<template>
    <div class="container py-4">
        <div class="row align-items-center">
            <div class="col-md-1">
            </div>
            <!-- Left: Image -->
            <div class="col-md-5 text-center">
                <img src="../assets/images/family.png" alt="Family" class="img-fluid" style="max-height: 500px;" />
            </div>
            <div class="col-md-1">
            </div>
            <!-- Right: Text -->
            <div class="col-md-5">
                <div class="font-semibold text-7xl">Help you secure your <br> <span
                        class="font-semibold text-7xl pb-2">Dream
                        Home</span></div>
                <p class="text-sm">We all need a place we can call home, where we can feel safe and
                    comfortable.While life takes you to unexpected places, love brings you home. What sets Destiny
                    Promoters
                    apart from other companies is the world class sales and marketing service we provide to the most
                    deluxe
                    projects in Bangalore at a feasible price.</p>
                <router-link to="/about-us" custom v-slot="{ navigate }"><button @click="navigate"
                        class="flex items-center text-sm cursor-pointer text-white bg-[#1A1A1A] px-4 py-2 rounded-lg">
                        About Us
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                            stroke="currentColor" class="size-6 w-4 h-3 ml-2">
                            <path stroke-linecap="round" stroke-linejoin="round"
                                d="M13.5 4.5 21 12m0 0-7.5 7.5M21 12H3" />
                        </svg>
                    </button>
                </router-link>
            </div>
        </div>
    </div>
</template>
