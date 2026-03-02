<template>
    <div class="container mx-auto px-4 py-8">

        <!-- Section Heading -->
        <div class="text-center mb-6">
            <div class="font-semibold text-7xl">Featured Properties</div>
            <p class="text-xs">Explore the best homes and investments tailored for you</p>
        </div>

        <!-- Carousel -->
        <el-carousel height="420px" :interval="5000" arrow="always" indicator-position="none">
            <el-carousel-item v-for="(chunk, index) in chunkedProperties" :key="'chunk-' + index">
                <!-- SAME GRID AS BEFORE -->
                <div class="row g-4">
                    <div v-for="property in chunk" :key="property.id" class="col-12 col-sm-6 col-lg-3">
                        <router-link v-if="property.slug"
                            :to="{ name: 'ListingDetails', params: { slug: property.slug } }"
                            class="text-decoration-none">
                            <div class="card h-100 shadow-sm border-0 rounded-3">

                                <!-- Image Section -->
                                <div class="relative p-2 pb-0">
                                    <img :src="property.image" class="w-full h-52 object-cover rounded-xl"
                                        alt="Property" />

                                    <!-- Status Badge -->
                                    <div class="absolute top-6 left-6">
                                        <span v-if="property.status" class="px-3 py-1 text-xs font-bold rounded-full"
                                            :class="badgeColors(property.status)">
                                            {{ property.status }}
                                        </span>
                                    </div>
                                </div>

                                <!-- Card Body -->
                                <div class="card-body">
                                    <h6 class="text-red-400 font-semibold text-[13px]">
                                        {{ property.title }}
                                    </h6>

                                    <div class="card-title fw-semibold mb-1 text-[13px]">
                                        {{ property.subtitle }}
                                    </div>

                                    <div class="text-xs mb-2 d-flex align-items-center">
                                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                                            stroke-width="2" stroke="currentColor" class="h-4 w-4 me-1">
                                            <path stroke-linecap="round" stroke-linejoin="round"
                                                d="M15 10.5a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
                                            <path stroke-linecap="round" stroke-linejoin="round"
                                                d="M19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1 1 15 0Z" />
                                        </svg>
                                        {{ property.location }}
                                    </div>

                                    <!-- Features -->
                                    <div class="d-flex flex-wrap gap-3 text-sm text-secondary">
                                        <span class="d-flex align-items-center gap-2">
                                            <img src="../assets/images/Bed.png" class="h-3" />
                                            {{ property.beds }}
                                        </span>

                                        <span class="d-flex align-items-center gap-2">
                                            <img src="../assets/images/Bath.png" class="h-3" />
                                            {{ property.baths }}
                                        </span>

                                        <span class="d-flex align-items-center gap-2">
                                            <img src="../assets/images/Sqft.png" class="h-3" />
                                            {{ property.sizes }}
                                        </span>
                                    </div>
                                </div>

                            </div>
                        </router-link>
                    </div>
                </div>
            </el-carousel-item>
        </el-carousel>

    </div>
</template>

<script setup>
import { ref, onMounted, computed, onMounted as mountedHook } from "vue"

const properties = ref([])
const itemsPerSlide = ref(4)

// Detect screen size
const updateItemsPerSlide = () => {
    if (window.innerWidth < 640) {
        itemsPerSlide.value = 1   // Mobile
    } else if (window.innerWidth < 1024) {
        itemsPerSlide.value = 2   // Tablet
    } else {
        itemsPerSlide.value = 4   // Desktop
    }
}

mountedHook(() => {
    updateItemsPerSlide()
    window.addEventListener("resize", updateItemsPerSlide)
})

onMounted(async () => {
    try {
        const res = await fetch(
            "/api/method/destiny_promoters_website.api.project_api.get_projects?tag=Featured-Properties"
        )
        const data = await res.json()

        properties.value = data.message.map(p => ({
            id: p.name,
            slug: p.route || p.url || null,
            title: p.heading_first || "Featured Property",
            subtitle: p.project_name,
            location: p.full_location,
            beds: p.bhk || "-",
            baths: p.bath || "-",
            sizes: p.super_built_up_area || "-",
            status: p.status,
            image: p.thumbnail
        }))
    } catch (err) {
        console.error(err)
    }
})

// Responsive chunks
const chunkedProperties = computed(() => {
    const chunks = []
    for (let i = 0; i < properties.value.length; i += itemsPerSlide.value) {
        chunks.push(properties.value.slice(i, i + itemsPerSlide.value))
    }
    return chunks
})

const badgeColors = () => "bg-black text-white"
</script>