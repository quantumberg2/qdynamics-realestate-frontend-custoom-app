<template>
    <div class="container mx-auto px-4 pt-14">

        <!-- Header -->
        <div class="pb-8">
            <div class="text-[35px] font-medium pb-2">
                Find Your Dream Property
            </div>
            <p class="text-black mt-2 text-[13px]">
                Welcome to <strong>Destiny Promoters</strong>, where your dream property awaits in every corner of our
                beautiful world. Explore our curated selection of properties, each offering a unique story and a chance
                to redefine your life.
            </p>
        </div>

        <!-- Search Input -->
        <div class="flex justify-center pb-4">
            <div class="relative w-[90%] max-w-3xl">
                <input type="text" placeholder="Search For A Property" v-model="searchQuery"
                    class="w-full px-4 py-3 pr-40 rounded-xl bg-gray-100 text-sm border-0 outline-none focus:ring-0" />

                <button
                    class="hidden md:flex absolute top-1/2 right-2 transform -translate-y-1/2 bg-black text-white px-5 py-2 rounded-lg text-sm items-center gap-2 hover:bg-gray-800">
                    <i class="bi bi-search text-base"></i>
                    Find Property
                </button>

                <div class="block md:hidden mt-4 text-center">
                    <button
                        class="bg-black text-white px-5 py-2 rounded-lg text-sm flex items-center gap-2 hover:bg-gray-800 mx-auto">
                        <i class="bi bi-search text-base"></i>
                        Find Property
                    </button>
                </div>
            </div>
        </div>

        <!-- Property Cards -->
        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">

            <template v-for="property in filteredProperties" :key="property.slug">
                <router-link v-if="property && property.slug"
                    :to="{ name: 'ListingDetails', params: { slug: property.slug } }"
                    class="rounded-xl overflow-hidden shadow-md border bg-white no-underline text-black hover:no-underline">
                    <!-- Image + Status Badge -->
                    <div class="relative p-2">
                        <img :src="property.thumbnail" alt="Property Image"
                            class="w-full h-52 object-cover rounded-xl" />

                        <div v-if="property.status"
                            class="absolute top-4 left-4 text-white text-[10px] px-3 py-1 rounded-full z-10 bg-black">
                            {{ property.status }}
                        </div>
                    </div>

                    <!-- Content -->
                    <div class="px-3 pb-3">
                        <div class="text-[13px] font-semibold">
                            {{ property.name }}
                        </div>

                        <div class="flex items-center justify-between gap-2 mt-1">
                            <div class="text-xs text-gray-800 max-w-[60%] line-clamp-2">
                                {{ property.description }}
                            </div>
                            <button
                                class="bg-black text-white px-2 py-1 rounded-lg hover:bg-gray-800 text-sm whitespace-nowrap">
                                Know More
                            </button>
                        </div>
                    </div>
                </router-link>
            </template>

        </div>

        <!-- Amenities -->
        <BuildingAmenities />
    </div>
</template>


<script setup>
import { ref, computed, onMounted, watch } from 'vue'
import { useRoute } from 'vue-router'
import BuildingAmenities from './BuildingAmenities.vue'

const route = useRoute()

const properties = ref([])
const searchQuery = ref('')
const loading = ref(false)

// -------- Utils --------
const stripHtml = (html) => {
    if (!html) return ''
    const div = document.createElement('div')
    div.innerHTML = html
    return div.textContent || div.innerText || ''
}

const truncateText = (text, limit = 40) => {
    if (!text) return ''
    return text.length > limit ? text.slice(0, limit) + '...' : text
}

// -------- API --------
const fetchProjects = async () => {
    loading.value = true
    try {
        const params = new URLSearchParams()

        if (route.query.status) {
            params.append('status', route.query.status)
        }

        const res = await fetch(
            `/api/method/destiny_promoters_website.api.project_api.get_projects?${params.toString()}`,
            { credentials: 'include' }
        )

        const data = await res.json()

        properties.value = (data.message || []).map(p => ({
            slug: p.url,                     // ✅ FIXED
            name: p.project_name,
            description: truncateText(stripHtml(p.description), 20),
            thumbnail: p.thumbnail,
            location: p.full_location,
            bhk: p.bhk,
            floors: p.floors,
            status: p.status
        }))
    } catch (err) {
        console.error('Error fetching properties:', err)
        properties.value = []
    } finally {
        loading.value = false
    }
}

// -------- Lifecycle --------
onMounted(fetchProjects)
watch(() => route.query.status, fetchProjects)

// -------- Search --------
const filteredProperties = computed(() => {
    const q = searchQuery.value.toLowerCase()
    return properties.value.filter(p =>
        p.slug &&
        p.name?.toLowerCase().includes(q)
    )
})
</script>
