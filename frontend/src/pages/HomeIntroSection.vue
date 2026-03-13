<template>
    <div class="container">
        <div class="row align-items-center">

            <!-- Content area with background -->
            <div class="row align-items-center">
                <!-- Left: Text -->
                <div class="col-md-7 p-4">
                    <div class="font-semibold text-7xl">
                        Let Us Take You to Your Dream Home
                    </div>
                    <div class="text-[14px]">
                        <p class=" mt-3 pb-1">
                            At Destiny Promoters, we believe that finding the right home is one of the most
                            important
                            decisions in a person's life. A home is not just a structure made of bricks and walls—it
                            is
                            a place where dreams grow, families come together, and lifelong memories are created.
                            Our
                            goal is to guide you on this journey and help you discover a home that perfectly fits
                            your
                            lifestyle, needs, and aspirations.
                        </p>
                        <p class="">
                            Destiny Promoters is a leading real estate agency in Bangalore, supported by a team of
                            experienced and dedicated professionals who are committed to delivering the highest
                            level of
                            service. With deep knowledge of the local real estate market and a strong network of
                            reputed
                            builders and developers, we ensure that our clients receive the best property options
                            available. Our approach focuses on transparency, trust, and customer satisfaction,
                            making
                            the entire property search and purchase process smooth and reliable.
                        </p>
                        <p class="">
                            With over five years of experience in the diversified real estate sector, Destiny
                            Promoters
                            has built a strong reputation for delivering quality services and maintaining long-term
                            relationships with clients. Our success is built on our commitment to professionalism,
                            integrity, and a distinctive approach that prioritizes the needs of our customers. We
                            take
                            pride in our impeccable track record, unique style of service, and consistently high
                            levels
                            of customer satisfaction.
                        </p>
                    </div>
                    <router-link to="/about-us" class="no-underline">
                        <button
                            class="flex items-center text-sm cursor-pointer text-white bg-[#1A1A1A] px-4 py-2 rounded-lg mt-3">
                            Discover
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                stroke="currentColor" class="size-6 w-4 h-3 ml-2">
                                <path stroke-linecap="round" stroke-linejoin="round"
                                    d="M13.5 4.5 21 12m0 0-7.5 7.5M21 12H3" />
                            </svg>
                        </button>
                    </router-link>
                </div>

                <!-- Right: Image -->
                <div class="col-md-5 text-center p-4">
                    <img src="../assets/images/home_intro.png" alt="Family" class="img-fluid"
                        style="max-height: 500px;" />
                </div>
            </div>

            <div class="col-md-1"></div>
        </div>
    </div>
</template>
