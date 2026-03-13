<template>
    <div>

        <!-- HERO SECTION -->
        <div class="relative w-full h-[80vh] overflow-hidden mb-16">

            <img src="../assets/images/Interiors/Interiors-1.png" class="absolute w-full h-full object-cover" />

            <!-- Overlay -->
            <div class="absolute inset-0 bg-black/50"></div>


            <router-link to="/listing" class="no-underline">
                <button
                    class="absolute top-[33%] right-[8%] bg-[#1a1a1a] text-white px-6 py-2 rounded-md flex items-center text-xs space-x-2 hover:bg-gray-800 transition duration-300 sm:text-xs sm:px-5 sm:py-[10px] xs:text-[10px] xs:px-4 xs:py-2">
                    Explore Projects <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                        stroke-width="1.5" stroke="currentColor" class="w-4 h-3">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5 21 12m0 0-7.5 7.5M21 12H3" />
                    </svg>
                </button>
            </router-link>

        </div>


        <!-- CATEGORY SECTION -->
        <div class="container mb-16">

            <div class="row align-items-center mb-10">

                <div class="col-md-6">
                    <div class="text-[#E7C873] font-medium mb-2">
                        CATEGORIES
                    </div>

                    <h2 class="text-5xl font-semibold">
                        Architecture Interior
                    </h2>
                </div>

                <div class="col-md-6 text-gray-600">
                    Designing an architectural interior involves integrating functionality,
                    aesthetics, and user experience to create spaces that are both visually
                    appealing and practical.
                </div>

            </div>


            <!-- CATEGORY CARDS -->
            <div class="row text-center">

                <div class="col-lg-3 col-md-6 mb-4" v-for="(item, i) in categories" :key="i">

                    <div class="p-3 rounded-xl hover:shadow-xl transition duration-300">

                        <img :src="item.image" class="img-fluid rounded-lg" />

                        <div class="mt-3 font-medium text-lg">
                            {{ item.name }}
                        </div>

                    </div>

                </div>

            </div>

        </div>



        <!-- STATS SECTION -->
        <div class="bg-[#1a1a1a] py-14 mb-16">

            <div class="container">

                <div class="grid grid-cols-2 md:grid-cols-4 text-center gap-10">

                    <div v-for="stat in stats" :key="stat.title">

                        <div class="text-4xl text-[#E7C873] font-bold">
                            {{ stat.number }}
                        </div>

                        <div class="text-[#E7C873] font-medium mt-1">
                            {{ stat.title }}
                        </div>

                        <div class="text-gray-300 text-sm">
                            {{ stat.desc }}
                        </div>

                    </div>

                </div>

            </div>

        </div>



        <!-- ABOUT SECTION -->
        <div class="container mb-20">

            <div class="row bg-gray-100 p-5 rounded-4 align-items-center">

                <div class="col-md-5">
                    <img src="../assets/images/Interiors/Interiors-6.png" class="img-fluid rounded" />
                </div>


                <div class="col-md-7 p-4">

                    <h2 class="text-4xl font-semibold text-[#E7C873] mb-4">
                        Turning Houses into Homes, One Design at a Time
                    </h2>

                    <div class="text-[14px]">
                        <p> At Destiny Promoters, we believe that a house becomes a true home when it reflects the
                            lifestyle, personality, and aspirations of the people who live in it. A home is more than
                            just a physical space—it is where comfort meets happiness, where families build their
                            future, and where countless memories are created over time. </p>
                        <p> With every project we undertake, we focus on blending thoughtful design, quality
                            construction, and modern living concepts to create spaces that are both functional and
                            beautiful. Our approach is centered on understanding the unique needs of our clients and
                            transforming those ideas into living spaces that truly feel personal and welcoming. </p>
                        <p> From smart space planning to elegant design elements, we ensure that every detail
                            contributes to a comfortable and inspiring environment. We believe that a well-planned home
                            improves not just the way people live, but also the way they experience everyday life. </p>
                        <p> Driven by innovation, professionalism, and a commitment to excellence, Destiny Promoters
                            continues to deliver homes that combine style, comfort, and lasting value. Our mission is
                            simple—to create spaces where people feel connected, relaxed, and proud to call their own,
                            turning houses into homes, one design at a time. 🏡 </p>
                    </div>

                    <router-link to="/listing">
                        <button class="bg-[#1a1a1a] hover:bg-black text-white px-5 py-2 rounded-full">
                            Explore Our Projects
                        </button>
                    </router-link>

                </div>

            </div>

        </div>



        <!-- GALLERY TITLE -->
        <div class="container mb-10">

            <div class="row align-items-center">

                <div class="col-md-6">

                    <div class="text-[#E7C873] font-medium">
                        GALLERY
                    </div>

                    <h2 class="text-5xl font-semibold">
                        Interior Design Gallery
                    </h2>

                </div>

                <div class="col-md-6 text-gray-600">
                    Develop a concept or theme that will guide you through the design process.
                </div>

            </div>

        </div>



        <!-- GALLERY GRID -->
        <div class="container mb-20">

            <div class="grid md:grid-cols-3 gap-4">

                <img src="../assets/images/Interiors/Interiors-7.png" class="rounded-lg w-full h-full object-cover" />

                <div class="grid gap-4">
                    <img src="../assets/images/Interiors/Interiors-8.png" class="rounded-lg" />
                    <img src="../assets/images/Interiors/Interiors-9.png" class="rounded-lg" />
                </div>

                <img src="../assets/images/Interiors/Interiors-10.png" class="rounded-lg w-full h-full object-cover" />

            </div>

        </div>


        <homesforyou />

    </div>
</template>



<script setup>

import homesforyou from './homesforyou.vue'

const categories = [
    {
        name: 'Classic',
        image: new URL('../assets/images/Interiors/Interiors-2.png', import.meta.url).href
    },
    {
        name: 'Modern',
        image: new URL('../assets/images/Interiors/Interiors-3.png', import.meta.url).href
    },
    {
        name: 'Minimalist',
        image: new URL('../assets/images/Interiors/Interiors-4.png', import.meta.url).href
    },
    {
        name: 'Contemporary',
        image: new URL('../assets/images/Interiors/Interiors-5.png', import.meta.url).href
    }
]


const stats = [
    {
        number: '348',
        title: 'Interior Projects',
        desc: 'Designing spaces that inspire'
    },
    {
        number: '5',
        title: 'Years Of Work',
        desc: 'Mastering expertise'
    },
    {
        number: '2K',
        title: 'Satisfied Clients',
        desc: 'Happy Clients'
    },
    {
        number: '99%',
        title: 'Happy Rate',
        desc: 'Customer satisfaction'
    }
]

</script>