<template>
    <div>
        <!-- First Section -->
        <div class="relative w-full h-auto mb-6">
            <!-- Background Image -->
            <img :src="constructionData.heroImage" alt="Construction Image" class="w-full h-auto object-cover" />
            <!-- Overlapping Button -->
            <button class="absolute top-[33%] right-[8%] bg-[#1a1a1a] text-white px-6 py-2 rounded-md flex items-center text-xs space-x-2 hover:bg-gray-800 transition duration-300
                 sm:text-xs sm:px-5 sm:py-[10px] 
                 xs:text-[10px] xs:px-4 xs:py-2">
                <span>{{ constructionData.buttonText }}</span>
                <span v-if="constructionData.buttonIcon">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                        stroke="currentColor" class="w-4 h-3">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5 21 12m0 0-7.5 7.5M21 12H3" />
                    </svg>
                </span>
            </button>
        </div>

        <!-- Second Section -->
        <div class="p-4 mb-6">
            <div class="font items-center bg-gray-100 p-5 rounded-4">
                <div class="row">
                    <div class="col-md-1"></div>
                    <!-- Left Image -->
                    <div class="col-md-5">
                        <img :src="constructionData.secondSection.image" alt="" />
                    </div>

                    <!-- Right Text -->
                    <div class="col-md-4 d-flex flex-column justify-content-center text-sm">
                        <div class="text-7xl font-semibold mb-3">{{ constructionData.secondSection.heading }}</div>

                        <p>There are many variations of content available, but <span
                                class="text-[#E7C873] font-semibold">Destiny Promoters</span> ensures originality and
                            quality, avoiding altered or random words that reduce impact.</p>

                        <ul class="list-disc pl-5">
                            <li v-for="(item, index) in constructionData.secondSection.list" :key="index">{{ item }}
                            </li>
                        </ul>
                    </div>
                    <div class="col-md-1"></div>
                </div>
            </div>
        </div>

        <!-- Third Section -->
        <div class="container font mb-5">
            <div class="row justify-content-center">
                <div
                    class="col-lg-8 col-md-10 col-10 bg-gray-100 rounded-pill py-4 d-flex flex-wrap justify-content-around align-items-center">
                    <div class="text-center px-3 mb-3 mb-md-0">
                        <div class="text-4xl md:text-7xl font-bold text-[#E7C873]">348</div>
                        <div class="text-sm font-medium">Winning Awards</div>
                    </div>
                    <div class="text-center px-3 mb-3 mb-md-0">
                        <div class="text-4xl md:text-7xl font-bold text-[#E7C873]">1000</div>
                        <div class="text-sm font-medium">Happy Clients</div>
                    </div>
                    <div class="text-center px-3 mb-3 mb-md-0">
                        <div class="text-4xl md:text-7xl font-bold text-[#E7C873]">10</div>
                        <div class="text-sm font-medium">Active Projects</div>
                    </div>
                    <div class="text-center px-3">
                        <div class="text-4xl md:text-7xl font-bold text-[#E7C873]">500</div>
                        <div class="text-sm font-medium">Engineer Members</div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Foruth Section-->
        <div class="bg-[#1a1a1a] py-5 mb-6">
            <div class="container-fluid px-4 px-md-5">
                <div class="row align-items-center">

                    <!-- Left Section -->
                    <div class="col-lg-7 col-md-7 col-12 mb-4 mb-md-0">
                        <div
                            class="text-white text-3xl sm:text-4xl md:text-6xl lg:text-7xl font-semibold leading-tight px-3">
                            Create the <span class="text-[#E7C873]">building</span><br>
                            <span>you want here</span>
                        </div>

                        <div class="text-white text-sm font-light py-4 px-3">
                            {{ constructionData.fourthSection.description }}
                        </div>

                        <div class="px-3">
                            <router-link to="/Listing" custom v-slot="{ navigate }">
                                <button @click="navigate"
                                    class="flex items-center text-sm cursor-pointer bg-white px-4 py-2 rounded-lg font no-underline">
                                    Projects
                                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                                        stroke-width="1.5" stroke="currentColor" class="size-6 w-4 h-3 ml-2">
                                        <path stroke-linecap="round" stroke-linejoin="round"
                                            d="M13.5 4.5 21 12m0 0-7.5 7.5M21 12H3" />
                                    </svg>
                                </button>
                            </router-link>
                        </div>
                    </div>

                    <div class="col-md-1"></div>

                    <!-- Right Section -->
                    <div class="col-lg-3 col-md-5 col-12 text-center text-md-end">
                        <img :src="constructionData.fourthSection.fourthImage" alt=""
                            class="img-fluid rounded-lg max-w-full h-auto">
                    </div>
                </div>
            </div>
        </div>

        <!-- Fifth Section -->
        <div class="container mb-6">
            <div class="row g-4 justify-content-center font">
                <div class="col-10 col-sm-6 col-lg-3">
                    <div class="border rounded-xl p-4 h-100">
                        <img src="../assets/images/Construction/5-card-1.png" alt="Industrial Solutions"
                            class="w-[33%] h-[33%] mb-5">
                        <h5 class="text-[#E7C873] font-semibold mb-2 text-[15px]">Industrial Solutions</h5>
                        <p class="text-xs">
                            We provide end-to-end infrastructure and construction services tailored for factories,
                            warehouses, and industrial spaces built for efficiency, durability, and scale.
                        </p>
                    </div>
                </div>

                <div class="col-10 col-sm-6 col-lg-3">
                    <div class="border rounded-xl p-4 h-100">
                        <img src="../assets/images/Construction/5-card-2.png" alt="Building Construction"
                            class="w-[33%] h-[33%] mb-5">
                        <h5 class="text-[#E7C873] font-semibold mb-2 text-[15px]">Building Construction</h5>
                        <p class="text-xs">
                            From concept to completion, we deliver reliable and high-quality construction services
                            for residential, commercial, and mixed-use buildings.
                        </p>
                    </div>
                </div>

                <!-- Card 3 -->
                <div class="col-10 col-sm-6 col-lg-3">
                    <div class="border rounded-xl p-4 h-100">
                        <img src="../assets/images/Construction/5-card-3.png" alt="Project Coordination"
                            class="w-[33%] h-[33%] mb-5">
                        <h5 class="text-[#E7C873] font-semibold mb-2 text-[15px]">Project Coordination</h5>
                        <p class="text-xs">
                            Seamless management of timelines, teams, and resources to ensure your construction projects
                            run smoothly from start to finish.
                        </p>
                    </div>
                </div>

            </div>
        </div>

        <!-- Sixth Section -->
        <homesforyou />

    </div>
</template>

<script setup>
import homesforyou from './homesforyou.vue';
const constructionData = {
    heroImage: new URL('../assets/images/Construction/construction.png', import.meta.url).href,
    buttonText: 'Contact Us',
    buttonIcon: true,

    secondSection: {
        image: new URL('../assets/images/Construction/construction_2.png', import.meta.url).href,
        heading: 'Most Modern & Powerful Work',
        list: [
            'Innovative Design Concepts',
            'Superior Build Quality',
            'Advanced Construction Techniques',
            'Smart Space Planning',
            'Sustainable Material Usage'
        ]
    },

    fourthSection: {
        description: 'Bring your dream space to life with Destiny Promoters. Whether you are envisioning a modern home, a commercial complex, or a personalized workspace — turn your ideas into reality with expert design, planning, and execution.',
        fourthImage: new URL('../assets/images/Construction/construction_3.png', import.meta.url).href
    }

}
</script>