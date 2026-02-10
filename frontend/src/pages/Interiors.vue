<template>
    <div>
        <!-- First Section -->
        <div class="relative w-full h-auto mb-6">
            <!-- Background Image -->
            <img src="../assets/images/Interiors/Interiors-1.png" alt="Interiors Image"
                class="w-full h-auto object-cover" />
            <!-- Overlapping Button -->

            <router-link to="/listing"><button
                    class="absolute top-[33%] right-[8%] flex items-center text-sm cursor-pointer bg-[#1a1a1a] px-4 py-2 rounded-lg text-white">
                    <span>Projects</span>
                    <span>
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                            stroke="currentColor" class="w-4 h-3">
                            <path stroke-linecap="round" stroke-linejoin="round"
                                d="M13.5 4.5 21 12m0 0-7.5 7.5M21 12H3" />
                        </svg>
                    </span>
                </button>
            </router-link>
        </div>

        <!-- Second Section -->
        <div class="container mb-3">
            <div class="row font col-lg-12 col-md-8 col-10 px-5 py-4">
                <div class="col-md-6">
                    <div class="text-[#E7C873] font-medium">CATEGORIES</div>
                    <div class="font-medium text-7xl py-4">Architecture Interior</div>
                </div>
                <div class="col-md-6">
                    <div class="text-[90%]">Designing an architectural interior involves integrating functionality,
                        aesthetics, and user experience to create spaces that are both visually
                        appealing and practical. Here's a step-by-step guide to designing an
                        architectural interior</div>
                </div>
            </div>
        </div>

        <!-- Third Section -->
        <div class="container">
            <div class="row justify-content-center text-center">
                <div class="col-lg-3 col-md-4 col-sm-6 col-10 mb-4">
                    <img src="../assets/images/Interiors/Interiors-2.png" alt="" class="img-fluid mx-auto d-block">
                    <div class="py-3 font-medium">Classic</div>
                </div>
                <div class="col-lg-3 col-md-4 col-sm-6 col-10 mb-4">
                    <img src="../assets/images/Interiors/Interiors-3.png" alt="" class="img-fluid mx-auto d-block">
                    <div class="py-3 font-medium">Modern</div>
                </div>
                <div class="col-lg-3 col-md-4 col-sm-6 col-10 mb-4">
                    <img src="../assets/images/Interiors/Interiors-4.png" alt="" class="img-fluid mx-auto d-block">
                    <div class="py-3 font-medium">Minimalist</div>
                </div>
                <div class="col-lg-3 col-md-4 col-sm-6 col-10 mb-4">
                    <img src="../assets/images/Interiors/Interiors-5.png" alt="" class="img-fluid mx-auto d-block">
                    <div class="py-3 font-medium">Contemporary</div>
                </div>
            </div>
        </div>

        <!-- Foruth Section-->
        <div class="bg-[#1a1a1a] py-4 mb-6">
            <div class="container px-4 px-md-5">
                <div class="row col-12 col-md-12 col-lg-12 justify-content-center text-center g-4">
                    <div class="col-md-2">
                        <div class="text-[220%] text-[#E7C873] font-bold">348</div>
                        <div class="text-[#E7C873]">Interior Projects</div>
                        <div class="text-sm text-white">Designing spaces that inspire, delight</div>
                    </div>
                    <div class="col-md-1"></div>
                    <div class="col-md-2">
                        <div class="text-[220%] text-[#E7C873] font-bold">5</div>
                        <div class="text-[#E7C873]">Years Of Work</div>
                        <div class="text-sm text-white">Mastering expertise, innovation</div>
                    </div>
                    <div class="col-md-1"></div>
                    <div class="col-md-2">
                        <div class="text-[220%] text-[#E7C873] font-bold">2K</div>
                        <div class="text-[#E7C873]">Satisfied Clients</div>
                        <div class="text-sm text-white">Happy Clients building lifelong relationships</div>
                    </div>
                    <div class="col-md-1"></div>
                    <div class="col-md-2">
                        <div class="text-[220%] text-[#E7C873] font-bold">99%</div>
                        <div class="text-[#E7C873]">Happy Rate</div>
                        <div class="text-sm text-white">Satisfaction rate, exceptions</div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Fifth Section -->
        <div class="p-4 mb-6">
            <div class="font items-center bg-gray-100 p-5 rounded-4">
                <div class="row">
                    <div class="col-md-1"></div>
                    <!-- Left Image -->
                    <div class="col-md-5">
                        <img src="../assets/images/Interiors/Interiors-6.png" alt="" />
                    </div>

                    <!-- Right Text -->
                    <div class="col-md-6 d-flex flex-column justify-content-center text-sm px-5">
                        <div class="text-[250%] font-bold mb-3 text-[#E7C873]">
                            Turning Houses into Homes, One Design at a Time
                        </div>

                        <div class="text-[110%] mb-4">
                            With every project we undertake, We are committed to turning houses
                            into homes, One design at a time
                        </div>

                        <router-link to="/listing" custom v-slot="{ navigate }">
                            <button @click="navigate"
                                class="inline-flex items-center text-sm cursor-pointer bg-[#1a1a1a] px-4 py-2 rounded-full text-white w-auto self-start">
                                Explore Our Projects
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                                    stroke-width="1.5" stroke="currentColor" class="size-6 w-4 h-3 ml-2">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M13.5 4.5 21 12m0 0-7.5 7.5M21 12H3" />
                                </svg>
                            </button>
                        </router-link>
                    </div>

                </div>
            </div>
        </div>

        <!-- Sixth Section -->
        <div class="container">
            <div class="row font col-lg-12 col-md-8 col-10 px-5 py-4">
                <div class="col-md-6">
                    <div class="text-[#E7C873] font-medium">GALLERY</div>
                    <div class="font-medium text-7xl py-4">Interior Design Gallery</div>
                </div>
                <div class="col-md-6">
                    <div class="text-[90%]">Develop a concept or theme that will guide you the design process. This
                        could be inspired by the client's preferences, the building's architecture, or a specific design
                        style.</div>
                </div>
            </div>
        </div>

        <!-- Seventh Section -->
        <div class="container mb-6">
            <div class="row g-3">
                <!-- First column: tall image -->
                <div class="col-lg-4 col-md-6">
                    <img src="../assets/images/Interiors/Interiors-7.png" alt=""
                        class="img-fluid rounded w-100 h-100 object-cover">
                </div>

                <!-- Second column: two stacked images -->
                <div class="col-lg-4 col-md-6 d-flex flex-column gap-3">
                    <img src="../assets/images/Interiors/Interiors-8.png" alt="" class="img-fluid rounded w-100">
                    <img src="../assets/images/Interiors/Interiors-9.png" alt="" class="img-fluid rounded w-100">
                </div>

                <!-- Third column: tall image -->
                <div class="col-lg-4 col-md-12">
                    <img src="../assets/images/Interiors/Interiors-10.png" alt=""
                        class="img-fluid rounded w-100 h-100 object-cover">
                </div>
            </div>
        </div>

        <!-- Eighth Section -->
        <homesforyou />

    </div>
</template>

<script setup>
import homesforyou from './homesforyou.vue';
</script>