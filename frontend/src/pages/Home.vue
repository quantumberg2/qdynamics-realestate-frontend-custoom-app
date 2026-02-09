<template>
  <div>
    <div class="container-fluid">
      <!-- First Section -->
      <div class="relative max-w-[1300px] mx-auto rounded-3xl overflow-hidden">
        <!-- Background Image -->
        <img src="/Home_Img_1.png" alt="Hero Banner" class="w-full h-[300px] sm:h-auto object-cover" />

        <!-- Overlay Content -->
        <div
          class="absolute inset-0 flex flex-col items-center justify-center text-white text-center px-2 sm:px-4 animate-slide-up">

          <!-- Heading -->
          <div
            class="text-[10px] sm:text-xs border border-white px-3 sm:px-4 py-1 sm:py-2 rounded-full tracking-wide mb-1 sm:mb-2">
            LET US GUIDE YOUR HOME
          </div>
          <div class="text-lg sm:text-3xl md:text-[45px] font-semibold mb-1 sm:mb-2">
            Enjoy The Finest Homes
          </div>
          <p class="text-[10px] sm:text-xs md:text-sm mb-4 sm:mb-8">
            From as low as $10 per day with limited time offer discounts
          </p>

          <!-- Filter Tabs -->
          <div
            class="flex items-center justify-center space-x-1 sm:space-x-2 bg-[#1a1a1a] text-white rounded-t-lg w-[130px] sm:w-[160px] md:w-[200px]">
            <button @click="setFilter('all')" :class="[
              'flex-1 py-2 sm:py-2 px-2 sm:px-3 text-[10px] sm:text-sm font-semibold rounded-tl-lg',
              selectedFilter === 'all' ? 'bg-white font' : 'hover:bg-gray-900 '
            ]">All</button>

            <button @click="setFilter('sale')" :class="[
              'flex-1 py-2 sm:py-2 px-2 sm:px-3 text-[10px] sm:text-sm rounded-t-lg',
              selectedFilter === 'sale' ? 'bg-white font' : 'hover:bg-gray-900'
            ]">Sale</button>

            <button @click="setFilter('rent')" :class="[
              'flex-1 py-2 sm:py-2 px-2 sm:px-3 text-[10px] sm:text-sm rounded-t-lg',
              selectedFilter === 'rent' ? 'bg-white font' : 'hover:bg-gray-900'
            ]">Rent</button>
          </div>

          <!-- Search Bar -->
          <div
            class="bg-white rounded-2xl sm:rounded-xl p-3 sm:p-2 shadow-lg w-[70%] sm:w-full sm:max-w-[50%] flex flex-col sm:flex-row items-stretch sm:items-center overflow-hidden">

            <!-- Keyword -->
            <div class="flex-1 border-b sm:border-b-0 sm:border-r pr-3 sm:pr-6  sm:mb-0">
              <label class="text-[10px] sm:text-xs text-gray-500 block text-left ml-2 sm:ml-3">Keyword</label>
              <input type="text" placeholder="Enter Keyword"
                class="w-full text-[10px] sm:text-sm border-0 outline-none py-0 focus:ring-0 text-black placeholder:text-black placeholder:text-[10px] sm:placeholder:text-xs" />
            </div>

            <!-- Type -->
            <div class="flex-1 border-b sm:border-b-0 sm:border-r px-2 sm:px-3 sm:mb-0">
              <label class="text-[10px] sm:text-xs text-gray-500 block text-left ml-2 sm:ml-3">Type</label>
              <select class="w-full text-[10px] sm:text-sm border-0 outline-none focus:ring-0 text-black py-0">
                <option>All Type</option>
                <option>House</option>
                <option>Apartment</option>
              </select>
            </div>

            <!-- Buttons -->
            <div class="flex gap-1 sm:gap-2 mt-2 sm:mt-0 sm:ml-2 justify-center">
              <!-- Filter Button -->
              <button
                class="flex items-center gap-1 px-2 sm:px-3 py-1 sm:py-2 text-[10px] sm:text-sm rounded-lg bg-white text-black border hover:bg-gray-100">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2"
                  stroke="currentColor" class="w-3 h-3 sm:w-4 sm:h-4">
                  <path stroke-linecap="round" stroke-linejoin="round"
                    d="M10.5 6h9.75M10.5 6a1.5 1.5 0 1 1-3 0m3 0a1.5 1.5 0 1 0-3 0M3.75 6H7.5m3 12h9.75m-9.75 0a1.5 1.5 0 0 1-3 0m3 0a1.5 1.5 0 0 0-3 0m-3.75 0H7.5m9-6h3.75m-3.75 0a1.5 1.5 0 0 1-3 0m3 0a1.5 1.5 0 0 0-3 0m-9.75 0h9.75" />
                </svg>
                Filter
              </button>

              <!-- Search Button -->
              <button
                class="px-3 sm:px-4 py-2 sm:py-2 text-[10px] sm:text-sm rounded-lg bg-[#1a1a1a] text-white hover:bg-gray-800">
                Search
              </button>
            </div>
          </div>
        </div>

        <!-- Stats: Show on Large Screens -->
        <div
          class="hidden md:block rounded-tl-[100px] overflow-hidden md:absolute md:bottom-[-25px] right-[-1px] w-[95%] md:w-[700px] mx-auto shadow-lg">
          <div class="grid grid-cols-1 md:grid-cols-3 gap-4 bg-white p-4 custom-clip items-start">

            <div class="text-left px-5">
              <div class="text-4xl font-bold">{{ soldOutCount }}+</div>
              <div class="text-sm text-gray-600 mt-1">Completed Projects</div>
            </div>

            <div class="text-left px-5">
              <div class="text-4xl font-bold">{{ upcomingCount }}+</div>
              <div class="text-sm text-gray-600 mt-1">Upcoming Projects</div>
            </div>

            <div class="text-left px-4">
              <div class="text-4xl font-bold">25+</div>
              <div class="text-sm text-gray-600 mt-1">Trained Professionals</div>
            </div>

          </div>
        </div>

      </div>

      <!-- Second Section -->
      <div class="pt-10">
        <div class="flex flex-col items-center relative">
          <div class="font-semibold text-5xl text-center">Homes For You</div>
          <div class="w-full flex justify-center mt-1">
            <div class="relative w-full max-w-6xl">
              <p class="text-sm text-center">Based on your view history</p>
              <router-link to="/Listing">
                <div class="absolute right-0 top-0 flex items-center text-sm cursor-pointer underline text-black">
                  View All
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2"
                    stroke="currentColor" class="w-4 h-3 ml-1">
                    <path stroke-linecap="round" stroke-linejoin="round" d="m4.5 19.5 15-15m0 0H8.25m11.25 0v11.25" />
                  </svg>
                </div>
              </router-link>
            </div>
          </div>
        </div>

        <!-- Carousel -->
        <el-carousel :interval="5000" arrow="always" height="350px" indicator-position="none">
          <el-carousel-item v-for="(chunk, index) in chunkedHomes" :key="'chunk-' + index">
            <div class="container px-5">
              <div class="container">
                <div class="row justify-content-center g-4">
                  <div class="col-md-4" v-for="(home, idx) in chunk" :key="'home-' + idx">
                    <router-link v-if="home.slug" :to="{ name: 'ListingDetails', params: { slug: home.slug } }"
                      class="text-decoration-none">
                      <div class="card h-100 shadow-sm border-0 rounded-3">
                        <div class="position-relative">
                          <img :src="home.thumbnail" class="card-img-top p-2 rounded-4" alt="Property Image"
                            style="height: 220px; object-fit: cover" />
                          <span class="position-absolute top-0 start-0 m-4 p-2 badge bg-dark rounded-5">
                            {{ home.status?.toUpperCase() || "UNKNOWN" }}
                          </span>
                        </div>
                        <div class="card-body">
                          <div class="card-title fw-semibold mb-1">{{ home.project_name }}</div>

                          <!-- Location -->
                          <p class="text-xs mb-3 d-flex align-items-center">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2"
                              stroke="currentColor" class="h-4 w-4 me-1">
                              <path stroke-linecap="round" stroke-linejoin="round"
                                d="M15 10.5a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
                              <path stroke-linecap="round" stroke-linejoin="round"
                                d="M19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1 1 15 0Z" />
                            </svg>
                            {{ home.full_location }}
                          </p>

                          <!-- Extra details -->
                          <div class="d-flex flex-wrap gap-3 text-xs text-secondary">
                            <span class="d-flex align-items-center gap-1">
                              <img src="../assets/images/Bed.png" alt="" class="h-3"> {{ home.bhk }}
                            </span>
                            <span class="d-flex align-items-center gap-1">
                              <img src="../assets/images/Bath.png" alt="" class="h-3"> {{ home.bath }}
                            </span>
                            <span class="d-flex align-items-center gap-1">
                              <img src="../assets/images/Sqft.png" alt="" class="h-3"> {{ home.super_built_up_area }}
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

      <!-- Stats: Show on small screens only -->
      <div
        class="block md:hidden bg-white p-4 w-[95%] mx-auto mt-4 grid grid-cols-1 text-center gap-4 rounded-xl shadow">
        <div>
          <div class="text-xl font-bold">{{ soldOutCount }}+</div>
          <div class="text-gray-500 text-sm">Completed Projects</div>
        </div>
        <div>
          <div class="text-xl font-bold">{{ upcomingCount }}+</div>
          <div class="text-gray-500 text-sm">Upcoming Projects</div>
        </div>
        <div>
          <div class="text-xl font-bold">25+</div>
          <div class="text-gray-500 text-sm">Trained Professionals</div>
        </div>
      </div>

      <!-- third Section -->
      <FeaturedCategories />

      <!-- Fourth Section -->
      <dreamhome />

      <!-- Fifth Section -->
      <FeaturedProperties />

      <!-- Sixth Section -->
      <CustomerTestimonials />

      <!-- seventh Section -->
      <HomeIntroSection />

      <!-- Eighth Section -->
      <BuildingAmenities />

    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { ElCarousel, ElCarouselItem } from 'element-plus'
import FeaturedProperties from './FeaturedProperties.vue'
import CustomerTestimonials from './CustomerTestimonials.vue'
import dreamhome from './dreamhome.vue'
import FeaturedCategories from './FeaturedCategories.vue'
import HomeIntroSection from './HomeIntroSection.vue'
import BuildingAmenities from './BuildingAmenities.vue'

const homes = ref([])

onMounted(async () => {
  try {
    // ✅ Call your backend API instead of static JSON
    const response = await fetch("/api/method/destiny_promoters_website.api.project_api.get_projects")
    if (!response.ok) throw new Error("Failed to fetch projects")
    const data = await response.json()

    // frappe returns { message: [...] }
    homes.value = data.message.map(project => ({
      id: project.name,                     // keep if needed internally
      slug: project.route || project.url,   // ✅ IMPORTANT
      project_name: project.project_name,
      status: project.status,
      full_location: project.full_location,
      bhk: project.bhk,
      bath: project.bath,
      super_built_up_area: project.super_built_up_area,
      builder: project.builder,
      thumbnail: project.thumbnail
    }))
  } catch (err) {
    console.error("Error loading projects:", err)
  }
})

// Filter logic
const selectedFilter = ref('all')

const filteredHomes = computed(() => {
  return selectedFilter.value === 'all'
    ? homes.value
    : homes.value.filter(h => h.status?.toLowerCase() === selectedFilter.value)
})

// Chunk homes (after filtering)
const chunkedHomes = computed(() => {
  const chunkSize = 3
  const chunks = []
  for (let i = 0; i < filteredHomes.value.length; i += chunkSize) {
    chunks.push(filteredHomes.value.slice(i, i + chunkSize))
  }
  return chunks
})

const soldOutCount = computed(() => {
  return homes.value.filter(
    h => h.status?.toLowerCase() === 'sold out'
  ).length
})

const upcomingCount = computed(() => {
  return homes.value.filter(
    h => h.status?.toLowerCase() === 'upcoming'
  ).length
})

const setFilter = filter => {
  selectedFilter.value = filter
}
</script>


<style scoped>
.custom-clip {
  clip-path: polygon(50 0, 100% 0%, 100% 100%, 0% calc(100% - 40px));
}

@keyframes slideUp {
  0% {
    transform: translateY(50px);
    opacity: 0;
  }

  100% {
    transform: translateY(0);
    opacity: 1;
  }
}

.animate-slide-up {
  animation: slideUp 0.8s ease-out forwards;
}
</style>