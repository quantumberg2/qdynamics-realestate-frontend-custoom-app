<template>
    <div class="container py-4">

        <!-- Page Title -->
        <div class="text-center mb-5">
            <h1 class="fw-bold">Interiors</h1>
            <p class="text-muted">Explore our project interiors images</p>
        </div>

        <!-- Loader -->
        <div v-if="loading" class="text-center py-5">
            <div class="spinner-border text-dark"></div>
            <p class="mt-3">Loading images...</p>
        </div>

        <!-- No Images -->
        <div v-if="!loading && images.length === 0" class="text-center py-5">
            <h5>No Images Found</h5>
        </div>

        <!-- Gallery Grid -->
        <div v-if="!loading" class="row g-4">
            <div v-for="(img, index) in images" :key="index" class="col-lg-4 col-md-6 col-sm-12">
                <div class="card border-0 shadow-sm overflow-hidden rounded-4 group cursor-pointer"
                    @click="openImage(img.image)">
                    <div class="overflow-hidden">
                        <img :src="img.image" :alt="img.alt_text"
                            class="w-100 h-64 object-cover transition duration-500 group-hover:scale-110" />
                    </div>
                </div>
            </div>
        </div>

        <!-- Popup Modal -->
        <div v-if="selectedImage"
            class="fixed inset-0 flex items-center justify-center z-50 bg-black/30 backdrop-blur-sm">
            <div class="relative flex justify-center items-center">

                <!-- Close Button -->
                <button
                    class="absolute -top-5 -right-5 bg-white rounded-full w-10 h-10 shadow-lg text-xl font-bold hover:bg-gray-200"
                    @click="closeImage">
                    ×
                </button>

                <!-- Full Image -->
                <img :src="selectedImage" class="max-h-[90vh] max-w-[90vw] object-contain rounded-3xl shadow-2xl" />

            </div>
        </div>

    </div>
</template>

<script setup>
import { ref, onMounted } from "vue"

const images = ref([])
const loading = ref(true)
const selectedImage = ref(null)

const fetchGallery = async () => {
    try {
        const res = await fetch(
            "/api/method/destiny_promoters_website.api.gallery.get_gallery_images"
        )

        const data = await res.json()
        images.value = data.message.data || []

    } catch (error) {
        console.error("Gallery API Error:", error)
    } finally {
        loading.value = false
    }
}

const openImage = (image) => {
    selectedImage.value = image
}

const closeImage = () => {
    selectedImage.value = null
}

onMounted(() => {
    fetchGallery()
})
</script>
