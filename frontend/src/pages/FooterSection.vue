<template>
    <div class="md:px-5 py-3">
        <footer class="bg-gray-50 rounded-2xl shadow-sm">
            <!-- Top -->
            <div class="flex flex-col md:flex-row items-center justify-between px-8 py-6">
                <!-- Logo -->
                <div class="flex items-center">
                    <img src="../assets/images/DP_Logo.png" alt="Destiny Promoters"
                        class="h-[60px] ml-4 md:ml-10 mt-2" />
                </div>

                <!-- Social -->
                <div class="flex items-center space-x-4 mt-4 md:mt-0">
                    <span class="font-medium text-sm">Follow Us</span>
                    <i class="fab fa-facebook-f text-sm cursor-pointer hover:text-gray-500"></i>
                    <i class="fab fa-twitter text-sm cursor-pointer hover:text-gray-500"></i>
                    <i class="fab fa-instagram text-sm cursor-pointer hover:text-gray-500"></i>
                    <i class="fab fa-linkedin-in text-sm cursor-pointer hover:text-gray-500"></i>
                </div>
            </div>

            <hr class="border-gray-400" />

            <!-- Main Grid -->
            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-6 gap-8 px-8 py-6 pb-5 pt-5">
                <!-- Subscribe -->
                <div class="col-span-1 md:col-span-2">
                    <h4 class="font-semibold mb-3 text-sm">Subscribe</h4>
                    <div class="flex items-center mb-3">
                        <input type="email" placeholder="Your e-mail"
                            class="w-50 h-8 px-3 text-sm border border-gray-300 rounded-l-full outline-none focus:ring-0" />
                        <button
                            class="bg-[#1a1a1a] text-white px-4 h-8 text-sm rounded-r-full flex items-center justify-center space-x-1">
                            <span>Send</span>
                            <span>→</span>
                        </button>
                    </div>
                    <p class="text-xs text-gray-800 pb-2">
                        Destiny Promoters have been in the diversified business of <br>real estate sector over the last
                        5 years.
                    </p>
                </div>


                <!-- Quick Links -->
                <div class="col-span-1">
                    <div class="font-semibold mb-3 text-sm">Quick Links</div>
                    <div class="space-y-2 text-xs text-black">

                        <div><router-link to="/AboutUs" class="font no-underline">About</router-link></div>
                        <div><router-link to="/contact-us" class="font no-underline">Contact</router-link></div>
                        <div><router-link to="/Listing" class="font no-underline">Listing</router-link></div>
                        <div><router-link to="/privacy-policy" class="font no-underline">Privacy Policy</router-link>
                        </div>
                        <div><router-link to="/terms-and-conditions" class="font no-underline">Terms &
                                Conditions</router-link></div>

                    </div>
                </div>

                <!-- Contact Us -->
                <div class="col-span-1 ">
                    <div class="font-semibold mb-3 text-sm">Contact Us</div>
                    <a href="mailto:sales@destinypromoters.in" class="block text-xs font no-underline">
                        sales@destinypromoters.in
                    </a>

                    <a href="tel:+919686450917" class="block text-xs font no-underline mt-1">
                        +91 96864 50917
                    </a>
                </div>

                <!-- Our Address -->
                <div class="col-span-1">
                    <div class="font-semibold mb-3 text-sm">Our Address</div>
                    <div class="text-xs text-black leading-snug">
                        #97/B (New #1/2), 1st Floor, Jayanagar
                        7th Block, Bangalore - 560082
                    </div>
                </div>

                <!-- Get the App -->
                <div class="col-span-1">
                    <div class="font-semibold mb-3 text-sm">Get the app</div>
                    <div class="space-y-3">
                        <button
                            class="bg-[#1a1a1a] text-white px-4 py-2 rounded-lg flex items-center space-x-4 sm:w-1/2 md:w-full text-sm">
                            <i class="fab fa-apple text-lg"></i>
                            <span class="text-left">
                                <span class="block text-xs font-light text-gray-200">Download on the</span>
                                <span class="font-semibold">Apple Store</span>
                            </span>
                        </button>

                        <button
                            class="bg-[#1a1a1a] text-white px-4 py-2 rounded-lg flex items-center space-x-4 sm:w-1/2 md:w-full text-sm">
                            <i class="fab fa-google-play text-lg"></i>
                            <span class="text-left">
                                <span class="block text-xs font-light text-gray-200">Get it on</span>
                                <span class="font-semibold">Google Play</span>
                            </span>
                        </button>

                    </div>
                </div>
            </div>


            <hr class="border-gray-400" />

            <!-- Bottom -->
            <div class="flex flex-col md:flex-row items-center px-8 py-2 text-xs text-black gap-10 md:gap-40 pb-5">
                <span>Copyright © 2025. Destiny Promoters</span>
                <span>Powered By: Quantumberg Technologies Pvt Ltd</span>
            </div>
        </footer>
    </div>
</template>

<script>
export default {
    name: "FooterSection",
};
</script>

<style scoped>
@import url("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css");
</style>