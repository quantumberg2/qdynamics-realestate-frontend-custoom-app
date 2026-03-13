<template>
    <div class="container py-4">
        <div class="row align-items-center">
            <div class="col-md-1">
            </div>
            <!-- Left: Image -->
            <div class="col-md-5 text-center">
                <img src="../assets/images/family.png" alt="Family" class="img-fluid object-cover rounded-3" style="max-height: 500px;" />
            </div>
            <!-- Right: Text -->
            <div class="col-md-6">
                <div class="font-semibold text-7xl mb-3">Helping You Secure Your Dream Home</div>
                <div class="text-[14px]">
                    <p class="">A home is more than just a place to live it is a space where comfort, security, and
                        happiness come together. It is where memories are created, families grow, and life finds its
                        true
                        meaning. In today's fast-paced world, life may take you to many unexpected places, but in the
                        end,
                        love always brings you back home.</p>

                    <p class="">At Destiny Promoters, we understand the emotional and financial importance of owning the
                        perfect home. Our mission is to help individuals and families find properties that not only meet
                        their needs but also fulfill their dreams of a better lifestyle. We carefully select and present
                        some of the most premium and well-planned real estate projects across Bangalore, ensuring that
                        our
                        clients receive the best options available in the market.</p>

                    <p class="">What truly sets Destiny Promoters apart is our commitment to delivering world-class
                        sales
                        and marketing services while maintaining transparency, trust, and customer satisfaction. Our
                        team
                        works closely with reputed builders and developers to bring you luxurious residential projects
                        at
                        feasible and competitive prices. From the initial consultation to the final purchase, we guide
                        you
                        through every step of the journey, making the home-buying process smooth, reliable, and
                        stress-free.
                    </p>
                </div>

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
