<template>
    <div>
        <!-- First Section -->
        <div class="relative w-full h-auto mb-6">
            <img src="../assets/images/ContactUS.png" alt="About Us Image" class="w-full h-auto object-cover" />
        </div>

        <!-- Second Section -->
        <div class="px-[7%]">
            <div class="row mb-5">
                <div class="col-md-5 rounded-3 bg-[#1a1a1a] px-[7%] py-[7%] text-white font ">
                    <div class="ml-12">
                        <!-- Contact Number -->
                        <div class="flex mb-[9%]">
                            <div
                                class="bg-[#E7C873] inline-flex items-center justify-center rounded-full w-10 h-10 mr-4">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                                    stroke-width="1.3" stroke="currentColor" class="w-4 h-4 font">
                                    <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 6.75c0 8.284 6.716 15 15 15h2.25
                            a2.25 2.25 0 0 0 2.25-2.25v-1.372
                            c0-.516-.351-.966-.852-1.091l-4.423-1.106
                            c-.44-.11-.902.055-1.173.417l-.97 1.293
                            c-.282.376-.769.542-1.21.38
                            a12.035 12.035 0 0 1-7.143-7.143
                            c-.162-.441.004-.928.38-1.21l1.293-.97
                            c.363-.271.527-.734.417-1.173L6.963 3.102
                            a1.125 1.125 0 0 0-1.091-.852H4.5
                            A2.25 2.25 0 0 0 2.25 4.5v2.25Z" />
                                </svg>
                            </div>
                            <div>
                                <div class="text-sm text-gray-200 mb-1">Contact Number</div>
                                <div class="font-semibold text-xl"> <a href="tel:+91 96864 50917"
                                        class="text-white no-underline">+91 96864 50917</a>
                                </div>
                            </div>
                        </div>

                        <!-- Email -->
                        <div class="flex mb-[9%]">
                            <div
                                class="bg-[#E7C873] inline-flex items-center justify-center rounded-full w-10 h-10 mr-4">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                                    stroke-width="1.3" stroke="currentColor" class="w-4 h-4 font">
                                    <path stroke-linecap="round" stroke-linejoin="round" d="M21.75 6.75v10.5a2.25 2.25 0 0 1-2.25 2.25H4.5
                            a2.25 2.25 0 0 1-2.25-2.25V6.75
                            m19.5 0A2.25 2.25 0 0 0 19.5 4.5H4.5
                            a2.25 2.25 0 0 0-2.25 2.25m19.5 0v.243
                            a2.25 2.25 0 0 1-1.07 1.916l-7.5 4.615
                            a2.25 2.25 0 0 1-2.36 0L3.82 8.91
                            A2.25 2.25 0 0 1 2.75 6.993V6.75" />
                                </svg>
                            </div>
                            <div>
                                <div class="text-sm text-gray-200 mb-1">E-mail</div>
                                <div class="font-semibold text-xl"><a href="mailto:sales@destinypromoters.in"
                                        class="text-white no-underline">sales@destinypromoters.in</a></div>
                            </div>
                        </div>

                        <!-- Location -->
                        <div class="flex mb-[9%]">
                            <div
                                class="bg-[#E7C873] inline-flex items-center justify-center rounded-full w-10 h-10 mr-4">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                                    stroke-width="1.3" stroke="currentColor" class="w-4 h-4 font">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M15 10.5a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1 1 15 0Z" />
                                </svg>


                            </div>
                            <div>
                                <div class="text-sm text-gray-200 mb-1">Location</div>
                                <div class="font-semibold text-xl">
                                    <a href="https://www.google.com/maps/place/Destiny+Promoters/@12.928273,77.577136,17z/data=!3m1!4b1!4m6!3m5!1s0x3bae15a26c2f1a79:0x5d1ffd246711ba32!8m2!3d12.928273!4d77.577136!16s%2Fg%2F11c24g0t5c"
                                        target="_blank" class="no-underline text-white">
                                        #97/B (New #1/2), 1st Floor,<br>
                                        Jayanagar 7th Block, Bangalore - 560082
                                    </a>
                                </div>

                            </div>
                        </div>

                        <!-- Social Media -->
                        <div class="mt-6 mb-[9%] text-gray-300 text-sm">
                            Stay updated with the latest listing and tips -<br>
                            Follow on social media!
                        </div>
                        <div class="flex space-x-4 mt-4 text-xs">
                            <i class="fab fa-facebook-f"></i>
                            <i class="fab fa-twitter"></i>
                            <i class="fab fa-instagram"></i>
                            <i class="fab fa-linkedin-in"></i>
                        </div>
                    </div>
                </div>
                <div class="col-md-1"></div>

                <!-- Contact Form -->
                <div class="col-md-6">
                    <contactForm />
                </div>
            </div>

            <!-- Second Section -->
            <div>
                <div class="text-[190%] font font-semibold mb-4">Location</div>
                <iframe
                    src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d243.04246662055274!2d77.57708218114766!3d12.928311223905348!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae15a26c2f1a79%3A0x5d1ffd246711ba32!2sDestiny%20Promoters!5e0!3m2!1sen!2sin!4v1754913585832!5m2!1sen!2sin"
                    class="w-full" height="450" style="border:0;" allowfullscreen="" loading="lazy"
                    referrerpolicy="no-referrer-when-downgrade"></iframe>
            </div>
        </div>

    </div>
</template>

<script setup>
import contactForm from './contactForm.vue';
</script>