<template>
    <div>
        <div class="relative w-full h-48 sm:h-64 md:h-80">
            <!-- Image -->
            <img src="/gallery.jpg" alt="gallery-banner-image" class="w-full h-full object-cover" />

            <!-- Black Overlay -->
            <div class="absolute inset-0 bg-black/30"></div>

            <!-- Text Content -->
            <div class="absolute inset-0 flex items-center">
                <div class="container mx-auto px-4 sm:px-6">
                    <h1 class="text-white font-semibold">
                        Gallery
                    </h1>
                </div>
            </div>
        </div>

        <div class="container mx-auto px-4 pt-14">

            <!-- ========================= -->
            <!-- PROPERTY CARDS -->
            <!-- ========================= -->
            <div v-if="!selectedProject" class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
                <div v-for="property in properties" :key="property.project" @click="selectProject(property)"
                    class="rounded-xl overflow-hidden shadow-md border bg-white cursor-pointer hover:shadow-lg transition">
                    <div class="p-2">
                        <img :src="property.thumbnail" alt="Property Image"
                            class="w-full h-52 object-cover rounded-xl" />
                    </div>

                    <div class="px-3 pb-3">
                        <div class="text-[13px] font-semibold text-center">
                            {{ property.project_name }}
                        </div>
                    </div>
                </div>
            </div>

            <!-- ========================= -->
            <!-- TAG BUTTONS + GALLERY -->
            <!-- ========================= -->
            <div v-else>

                <!-- Back Button -->
                <button @click="resetGallery" class="mb-6 text-sm text-black hover:underline">
                    ← Back to Properties
                </button>

                <!-- Property Title -->
                <h2 class="text-xl font-semibold mb-4">
                    {{ selectedProject.project_name }}
                </h2>

                <!-- TAG BUTTONS -->
                <div class="flex flex-wrap gap-3 mb-6">
                    <button v-for="tag in tags" :key="tag" @click="selectTag(tag)" :class="[
                        'px-4 py-1 rounded-full text-sm border transition',
                        activeTag === tag
                            ? 'bg-black text-white'
                            : 'bg-white text-black hover:bg-gray-100'
                    ]">
                        {{ tag }}
                    </button>
                </div>

                <!-- GALLERY IMAGES -->
                <div v-if="images.length" class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
                    <div v-for="img in images" :key="img.name" class="rounded-lg overflow-hidden shadow">
                        <img :src="img.image" class="w-full h-52 object-cover" alt="Gallery Image" />
                    </div>
                </div>


                <div v-else class="text-gray-500 text-sm">
                    No images found for this tag.
                </div>

                <div class="mt-8 flex justify-center">
                    <button @click="goToDetails"
                        class="bg-black text-white px-6 py-2 rounded-xl text-sm hover:bg-gray-800 transition">
                        Learn More About the Property
                    </button>
                </div>


            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from "vue"
import { useRouter } from "vue-router"

const router = useRouter()

/* ---------------------------
   STATE
----------------------------*/
const properties = ref([])
const selectedProject = ref(null)
const tags = ref([])
const images = ref([])
const activeTag = ref(null)

/* ---------------------------
   FETCH PROJECTS
----------------------------*/
const fetchProperties = async () => {
    const res = await fetch(
        "/api/method/destiny_promoters_website.api.project_api.get_gallery_projects"
    )
    const data = await res.json()
    properties.value = data.message || []
}

/* ---------------------------
   ACTIONS
----------------------------*/
const selectProject = (property) => {
    selectedProject.value = property
    activeTag.value = null
    images.value = []

    // Extract tags from custom_gallery
    tags.value = property.custom_gallery?.map(g => g.select_tag) || []

    // Auto-select first tag
    if (tags.value.length) {
        selectTag(tags.value[0])
    }
}

const selectTag = (tag) => {
    activeTag.value = tag

    const gallery = selectedProject.value.custom_gallery?.find(
        g => g.select_tag === tag
    )

    images.value = gallery
        ? gallery.images.map((img, index) => ({
            name: index,
            image: img
        }))
        : []
}

const resetGallery = () => {
    selectedProject.value = null
    tags.value = []
    images.value = []
    activeTag.value = null
}

/* ---------------------------
   GO TO DETAILS
----------------------------*/
const goToDetails = () => {
    if (!selectedProject.value?.url) return

    router.push({
        name: "ListingDetails",
        params: { slug: selectedProject.value.url }
    })
}

/* ---------------------------
   INIT
----------------------------*/
onMounted(fetchProperties)
</script>
