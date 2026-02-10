<template>
    <div>
        <div></div>
        <!-- First Section -->
        <div class="relative w-full h-auto mb-6">
            <!-- Background Image -->
            <img :src="aboutData.heroImage" alt="About Us Image" class="w-full h-auto object-cover" />

            <!-- Overlapping Button -->
            <button class="absolute top-[78%] right-[8%] bg-[#1a1a1a] text-white px-6 py-2 rounded-md flex items-center text-xs space-x-2 hover:bg-gray-800 transition duration-300
                 sm:text-xs sm:px-5 sm:py-[10px] 
                 xs:text-[10px] xs:px-4 xs:py-2">
                <span>{{ aboutData.buttonText }}</span>
                <span v-if="aboutData.buttonIcon">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                        stroke="currentColor" class="w-4 h-3">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5 21 12m0 0-7.5 7.5M21 12H3" />
                    </svg>
                </span>
            </button>
        </div>

        <!-- Heading and Intro Section -->
        <div class="container row">
            <div class="col-md-2"></div>
            <div class="col-md-8">
                <div class="text-[#E7C873] font-extrabold italic mb-0 text-7xl">
                    {{ aboutData.headingOne }}
                </div>
            </div>
        </div>

        <div class="container row mb-4">
            <div class="col-md-2"></div>
            <div class="col-md-8">
                <div class="font font-medium mb-0 text-7xl">
                    {{ aboutData.headingTwo }}
                </div>
            </div>
        </div>

        <div class="container row">
            <div class="col-md-2"></div>
            <div class="col-md-8">
                <div class="text-sm font">
                    <p v-html="aboutData.introText"></p>
                </div>
            </div>
        </div>

        <!-- Second Section -->
        <div class="container pt-8 mb-6">
            <div class="row font">
                <div class="col-md-4"></div>
                <div class="text-sm px-4 sm:px-8 md:px-12 col-md-3 mb-3">
                    <div class="mb-2 font-semibold text-2xl">{{ aboutData.missionVision.mission.title }}</div>
                    {{ aboutData.missionVision.mission.description }}
                </div>
                <div class="col-md-1"></div>
                <div class="text-sm px-4 sm:px-8 md:px-12 col-md-3">
                    <div class="mb-2 font-semibold text-2xl">{{ aboutData.missionVision.vision.title }}</div>
                    {{ aboutData.missionVision.vision.description }}
                </div>
            </div>
        </div>

        <!-- Third Section -->
        <div class="p-3">
            <div class="container bg-gray-100 rounded-4 py-4 font mb-6">
                <div class="row">
                    <div class="col-md-1 mb-3"></div>
                    <div class="col-md-7 text-sm">
                        <div class="text-7xl font-semibold mb-2">{{ aboutData.letUsHeading }}</div>
                        <p v-for="(para, index) in aboutData.letUsContent" :key="index">{{ para }}</p>

                        <router-link to="/Listing" custom v-slot="{ navigate }">
                            <button @click="navigate"
                                class="flex items-center text-sm cursor-pointer bg-[#1a1a1a] px-4 py-2 rounded-lg text-white">
                                Projects
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                                    stroke-width="1.5" stroke="currentColor" class="size-6 w-4 h-3 ml-2">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M13.5 4.5 21 12m0 0-7.5 7.5M21 12H3" />
                                </svg>
                            </button>
                        </router-link>
                    </div>
                    <div class="col-md-3">
                        <img :src="aboutData.letUsImage" alt="" />
                    </div>
                </div>
            </div>
        </div>

        <!-- Fourth Section -->
        <div class="container font items-center pb-4">
            <div class="row">
                <!-- Left Image -->
                <div class="col-md-6">
                    <img :src="aboutData.fourthSection.image" alt="" />
                </div>

                <!-- Right Text -->
                <div class="col-md-6 d-flex flex-column justify-content-center text-sm">
                    <div class="text-7xl font-semibold mb-3">{{ aboutData.fourthSection.heading }}</div>

                    <p>If you're looking for total peace of mind for your real estate needs, <span
                            class="text-[#E7C873]">Destiny Promoters</span> is the company for you because for us
                        clients come first, and we'll be there for you at every step of the way.</p>

                    <ul class="list-disc pl-5">
                        <li v-for="(item, index) in aboutData.fourthSection.list" :key="index">{{ item }}</li>
                    </ul>

                    <p class="bg-gray-50 p-1 rounded-5 text-center font-bold">
                        {{ aboutData.fourthSection.highlight }}
                    </p>

                    <p>{{ aboutData.fourthSection.closing }}</p>
                </div>
            </div>
        </div>

        <!-- Reusable Component -->
        <!-- <homesforyou /> -->
    </div>
</template>

<script setup>
import homesforyou from './homesforyou.vue';

const aboutData = {
    heroImage: new URL('../assets/images/AboutUs/AboutUs.png', import.meta.url).href,
    buttonText: 'Contact Us',
    buttonIcon: true,

    headingOne: 'Explore your real estate dream into reality.',
    headingTwo: 'sharing home since 2020',
    introText: `At Destiny Promoters, we're redefining how people find homes by blending smart technology with <br> human expertise. Our mission is to make real estate simple, transparent, and personalized for <br> every client.`,

    missionVision: {
        mission: {
            title: 'Mission',
            description: 'Our mission is to simplify property ownership through trust, transparency, expertise, care, commitment, and innovation.'
        },
        vision: {
            title: 'Vision',
            description: 'Our vision is to redefine real estate experience through innovation, excellence, accessibility, trust, technology, and lasting value.'
        }
    },

    letUsImage: new URL('../assets/images/AboutUs/About_2.png', import.meta.url).href,
    letUsHeading: 'Let us take you to your home.',
    letUsContent: [
        'Destiny Promoters is a leading real estate agency with a team of experienced professionals who are dedicated to providing clients with the highest level of service available anywhere in Bangalore.',
        'Out of all the dreams of a person owning a dream house is the closest one to heart. But with the rising population and skyrocketing rates it is not a cake walk to own a house that you desire. Destiny Promoters have been in the diversified business of real estate sector over the last 5 years. It is known for its impeccable record of distinctive style and high customer satisfaction levels.',
        'The company is just not limited to its marketing and sales services it is even proving its metal in the diversified services of Project Management, Interior Designing and Financial assistance. It has branched out into all those services that guide a customer into getting a dream house. It doesn\'t just help you buy a house but helps you in getting the finances for it and design it exactly how you imagined your abode to be.'
    ],

    fourthSection: {
        image: new URL('../assets/images/AboutUs/AboutUs_3.png', import.meta.url).href,
        heading: 'The ideas and spaces behind your dreams',
        list: [
            'Exceptional customer service.',
            'Exceptional customer service.',
            'Exceptional customer service.',
            'Exceptional customer service.'
        ],
        highlight: 'Destiny Promoters embodies integrity, honesty and wisdom in all we do',
        closing: 'We understand that your home is more than just a commodity — it\'s where you live and raise your family.'
    }
};
</script>
