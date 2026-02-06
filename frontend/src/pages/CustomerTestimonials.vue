<template>
    <div class="p-4">
        <div class="bg-gray-50 pb-5 rounded-3">
            <!-- Full width gray background -->

            <div class="container px-5">
                <!-- Inside container -->
                <!-- Top row: heading & stats -->
                <div class="flex flex-col lg:flex-row justify-between items-start lg:items-center mb-10 pt-5">
                    <div class="text-7xl font-semibold leading-snug">
                        What our customers are <br> saying us?
                    </div>
                    <div class="flex gap-10 mt-4 lg:mt-0">
                        <div>
                            <div class="text-2xl font-bold">1K+</div>
                            <p class="text-gray-500 text-sm">Happy People</p>
                        </div>
                        <div>
                            <div class="text-2xl font-bold">4.88</div>
                            <div class="text-gray-500 text-sm">Overall rating</div>
                            <div class="flex text-yellow-400 mt-1 text-xs">
                                <i class="bi bi-star-fill"></i>
                                <i class="bi bi-star-fill"></i>
                                <i class="bi bi-star-fill"></i>
                                <i class="bi bi-star-fill"></i>
                                <i class="bi bi-star-half"></i>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Bottom row: Testimonials -->
                <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
                    <div v-for="(testimonial, index) in testimonials" :key="index"
                        class="bg-white p-6 rounded-xl shadow-sm flex flex-col justify-between">
                        <div class="flex items-center gap-4 mb-4">
                            <img :src="testimonial.image" class="w-12 h-12 rounded-full object-cover" alt="Customer" />
                            <div>
                                <div class="font-semibold">{{ testimonial.name }}</div>
                                <div class="text-gray-500 text-sm">{{ testimonial.role }}</div>
                            </div>
                            <div>
                                <img :src="testimonial.image1" alt="" class="w-50 sm:w-full">
                            </div>
                        </div>
                        <p class="text-gray-600 text-sm">{{ testimonial.feedback }}</p>
                    </div>
                </div>

            </div>
        </div>
    </div>
</template>

<script setup>

const testimonials = [
    {
        name: "Cameron Williamson",
        role: "Designer",
        image: new URL("../assets/images/test1.png", import.meta.url).href,
        image1: new URL("../assets/images/upcoma.png", import.meta.url).href,
        feedback:
            "Searches for multiplexes, property comparisons, and the loan estimator. Works great. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore."
    },
    {
        name: "Esther Howard",
        role: "Marketing",
        image: new URL("../assets/images/test2.png", import.meta.url).href,
        image1: new URL("../assets/images/upcoma.png", import.meta.url).href,
        feedback:
            "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae."
    },
    {
        name: "Devon Lane",
        role: "Developer",
        image: new URL("../assets/images/test3.png", import.meta.url).href,
        image1: new URL("../assets/images/upcoma.png", import.meta.url).href,
        feedback:
            "Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est."
    }
];
</script>
<style>
@import "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css";
</style>
