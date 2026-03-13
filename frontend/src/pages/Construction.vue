<template>
    <div>

        <!-- HERO SECTION -->
        <div class="relative w-full h-[80vh] overflow-hidden mb-20">

            <img :src="constructionData.heroImage" class="absolute w-full h-full object-cover" />

            <div class="absolute inset-0 bg-black/50"></div>
            <!-- Overlapping Button --> 
             <router-link to="contact-us">
                <button
                    class="absolute top-[33%] right-[8%] bg-[#1a1a1a] text-white px-6 py-2 rounded-md flex items-center text-xs space-x-2 hover:bg-gray-800 transition duration-300 sm:text-xs sm:px-5 sm:py-[10px] xs:text-[10px] xs:px-4 xs:py-2">
                    <span>{{ constructionData.buttonText }}</span> <span v-if="constructionData.buttonIcon"> 
                        <svg
                            xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                            stroke="currentColor" class="w-4 h-3">
                            <path stroke-linecap="round" stroke-linejoin="round"
                                d="M13.5 4.5 21 12m0 0-7.5 7.5M21 12H3" />
                        </svg> 
                    </span> 
                </button> 
            </router-link>
        </div>



        <!-- ABOUT SECTION -->
        <div class="container mb-20">

            <div class="row align-items-center bg-gray-100 p-5 rounded-4">

                <div class="col-md-5 mb-4 mb-md-0">
                    <img :src="constructionData.secondSection.image" class="img-fluid rounded-3" />
                </div>


                <div class="col-md-7">

                    <h2 class="text-4xl md:text-5xl font-semibold mb-4">
                        {{ constructionData.secondSection.heading }}
                    </h2>

                    <p class="text-gray-700 text-sm mb-3">
                        At Destiny Promoters, we focus on delivering modern, high-quality real estate solutions that
                        combine innovation, functionality, and lasting value.
                    </p>

                    <ul class="list-disc pl-5 text-sm text-gray-700 space-y-2">

                        <li v-for="(item, index) in constructionData.secondSection.list" :key="index">

                            {{ item }}

                        </li>

                    </ul>

                </div>

            </div>

        </div>



        <!-- STATS SECTION -->
        <div class="container mb-20">

            <div class="bg-gray-100 rounded-full py-8">

                <div class="grid grid-cols-2 md:grid-cols-4 text-center gap-6">

                    <div>

                        <div class="text-4xl md:text-6xl font-bold text-[#E7C873]">
                            348
                        </div>

                        <div class="text-sm font-medium">
                            Winning Awards
                        </div>

                    </div>


                    <div>

                        <div class="text-4xl md:text-6xl font-bold text-[#E7C873]">
                            1000
                        </div>

                        <div class="text-sm font-medium">
                            Happy Clients
                        </div>

                    </div>


                    <div>

                        <div class="text-4xl md:text-6xl font-bold text-[#E7C873]">
                            10
                        </div>

                        <div class="text-sm font-medium">
                            Active Projects
                        </div>

                    </div>


                    <div>

                        <div class="text-4xl md:text-6xl font-bold text-[#E7C873]">
                            500
                        </div>

                        <div class="text-sm font-medium">
                            Engineer Members
                        </div>

                    </div>

                </div>

            </div>

        </div>



        <!-- CTA SECTION -->
        <div class="bg-[#1a1a1a] py-20 mb-20">

            <div class="container">

                <div class="row align-items-center">

                    <div class="col-md-7 text-white mb-4 mb-md-0">

                        <h2 class="text-4xl md:text-6xl font-semibold mb-4">

                            Create the
                            <span class="text-[#E7C873]">building</span>
                            you want here

                        </h2>

                        <p class="text-sm mb-3">
                            {{ constructionData.fourthSection.description1 }}
                        </p>

                        <p class="text-sm mb-4">
                            {{ constructionData.fourthSection.description2 }}
                        </p>

                        <router-link to="/listing">

                            <button class="bg-white text-black px-5 py-2 rounded-lg flex items-center gap-2">

                                Projects

                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                                    stroke-width="1.5" stroke="currentColor" class="w-4 h-4">

                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M13.5 4.5 21 12m0 0-7.5 7.5M21 12H3" />

                                </svg>

                            </button>

                        </router-link>

                    </div>



                    <div class="col-md-5 text-center">

                        <img :src="constructionData.fourthSection.fourthImage" class="img-fluid rounded-lg" />

                    </div>

                </div>

            </div>

        </div>



        <!-- SERVICES CARDS -->
        <div class="container mb-20">

            <div class="row justify-content-center g-4">

                <div class="col-md-4">

                    <div class="border rounded-xl p-5 h-100 hover:shadow-xl transition">

                        <img src="../assets/images/Construction/5-card-1.png" class="w-[30%] mb-5" />

                        <h5 class="text-[#E7C873] font-semibold mb-2">
                            Industrial Solutions
                        </h5>

                        <p class="text-sm">
                            We provide end-to-end infrastructure and construction services tailored for factories,
                            warehouses, and industrial spaces built for efficiency, durability, and scale.
                        </p>

                    </div>

                </div>



                <div class="col-md-4">

                    <div class="border rounded-xl p-5 h-100 hover:shadow-xl transition">

                        <img src="../assets/images/Construction/5-card-2.png" class="w-[30%] mb-5" />

                        <h5 class="text-[#E7C873] font-semibold mb-2">
                            Building Construction
                        </h5>

                        <p class="text-sm">
                            From concept to completion, we deliver reliable and high-quality construction services
                            for residential, commercial, and mixed-use buildings.
                        </p>

                    </div>

                </div>



                <div class="col-md-4">

                    <div class="border rounded-xl p-5 h-100 hover:shadow-xl transition">

                        <img src="../assets/images/Construction/5-card-3.png" class="w-[30%] mb-5" />

                        <h5 class="text-[#E7C873] font-semibold mb-2">
                            Project Coordination
                        </h5>

                        <p class="text-sm">
                            Seamless management of timelines, teams, and resources to ensure your construction
                            projects run smoothly from start to finish.
                        </p>

                    </div>

                </div>

            </div>

        </div>



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
            'Innovative Design Concepts - Creating modern and aesthetically pleasing spaces that blend style with functionality.',
            'Superior Build Quality - Ensuring strong construction standards that provide durability and long-term value.',
            'Advanced Construction Techniques - Using modern technologies and methods to deliver efficient and high-quality developments.',
            'Smart Space Planning - Designing layouts that maximize space utilization while maintaining comfort and convenience.',
            'Sustainable Material Usage - Promoting environmentally responsible construction with durable and eco-friendly materials.'
        ]
    },

    fourthSection: {
        description1: 'Bring your dream space to life with Destiny Promoters. Whether you are planning a modern home, a commercial complex, or a customized workspace, we are here to transform your vision into reality. With expert planning, innovative design, and professional execution, we ensure that every project reflects quality, functionality, and style.',
        description2: 'Our team works closely with clients to understand their unique requirements and deliver spaces that are thoughtfully designed and perfectly suited to their needs. From concept to completion, Destiny Promoters is committed to building spaces that inspire comfort, productivity, and long-term value.',
        fourthImage: new URL('../assets/images/Construction/construction_3.png', import.meta.url).href
    }

}
</script>