<!-- <template>
    <div class="px-4">
        <div class="container-fluid bg-gray-50 rounded-2xl mx-auto py-4 px-4">
            <div class="flex flex-col items-center relative">
                <div class="font-semibold text-5xl text-center">Homes For You</div>
                <div class="w-full flex justify-center mt-1">
                    <div class="relative w-full max-w-6xl">
                        <p class="text-sm text-center">Based on your view history</p>
                        <router-link to="/Listing">
                            <div
                                class="absolute right-0 top-0 flex items-center text-sm cursor-pointer underline text-black">
                                View All
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2"
                                    stroke="currentColor" class="w-4 h-3 ml-1">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="m4.5 19.5 15-15m0 0H8.25m11.25 0v11.25" />
                                </svg>
                            </div>
                        </router-link>
                    </div>
                </div>
            </div>

            <el-carousel :interval="5000" arrow="always" height="350px" indicator-position="none">
                <el-carousel-item v-for="(chunk, index) in chunkedHomes" :key="'chunk-' + index">
                    <div class="container px-5">
                        <div class="container">
                            <div class="row justify-content-center g-4">
                                <div class="col-md-4" v-for="(home, idx) in chunk" :key="'home-' + idx">
                                    <router-link :to="{ name: 'ListingDetails', params: { id: home.id } }"
                                        class="text-decoration-none">
                                        <div class="card h-100 shadow-sm border-0 rounded-3">
                                            <div class="position-relative">
                                                <img :src="home.image" class="card-img-top p-2 rounded-4"
                                                    alt="Property Image" style="height: 220px; object-fit: cover" />
                                                <span
                                                    class="position-absolute top-0 start-0 m-4 p-2 badge bg-dark rounded-5">
                                                    {{ home.type === 'ready' ? 'READY TO OCCUPY' :
                                                        home.type.toUpperCase() }}
                                                </span>
                                            </div>
                                            <div class="card-body">
                                                <div class="card-title fw-semibold mb-1">{{ home.title }}</div>
                                                <p class="text-xs mb-3 d-flex align-items-center">
                                                    <svg xmlns="http://www.w3.org/2000/svg" fill="none"
                                                        viewBox="0 0 24 24" stroke-width="2" stroke="currentColor"
                                                        class="h-4 w-4 me-1">
                                                        <path stroke-linecap="round" stroke-linejoin="round"
                                                            d="M15 10.5a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
                                                        <path stroke-linecap="round" stroke-linejoin="round"
                                                            d="M19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1 1 15 0Z" />
                                                    </svg>
                                                    {{ home.location }}
                                                </p>
                                                <div class="d-flex flex-wrap gap-3 text-xs text-secondary">
                                                    <span class="d-flex align-items-center gap-1">
                                                        <img src="../assets/images/Bed.png" alt="" class="h-3"> {{
                                                            home.beds }}
                                                    </span>
                                                    <span class="d-flex align-items-center gap-1">
                                                        <img src="../assets/images/Bath.png" alt="" class="h-3"> {{
                                                            home.baths }}
                                                    </span>
                                                    <span class="d-flex align-items-center gap-1">
                                                        <img src="../assets/images/Sqft.png" alt="" class="h-3"> {{
                                                            home.area }}
                                                    </span>
                                                </div>
                                            </div>
                                        </div>
                                    </router-link>
                                </div>
                            </div>
                        </div>
                    </div>
                </el-carousel-item>
            </el-carousel>
        </div>
    </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { ElCarousel, ElCarouselItem } from 'element-plus'

const homes = ref([])

onMounted(async () => {
    try {
        const response = await fetch("/assets/destiny_promoters_website/data/properties.json")
        if (!response.ok) throw new Error("Failed to fetch properties.json")
        const data = await response.json()

        homes.value = data.map(project => ({
            id: project.id,
            title: project.name,
            location: project.location,
            beds: project.bhk || "-",
            baths: project.bath || "-",
            area: project.superBuiltUpArea,
            type: project.status?.toLowerCase() || "unknown",
            image: project.thumbnail
        }))
    } catch (err) {
        console.error("Error loading properties:", err)
    }
})

// ✅ Chunk directly from homes
const chunkedHomes = computed(() => {
    const chunkSize = 3
    const chunks = []
    for (let i = 0; i < homes.value.length; i += chunkSize) {
        chunks.push(homes.value.slice(i, i + chunkSize))
    }
    return chunks
})
</script> -->
