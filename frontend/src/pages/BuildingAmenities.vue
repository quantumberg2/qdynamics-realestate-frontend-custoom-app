<template>
    <div class="container mx-auto px-4 py-8">
        <!-- Section Heading -->
        <div class="text-center mb-8">
            <div class="font-semibold text-7xl">Building Amenities</div>
        </div>

        <!-- Amenities Grid -->
        <div class="grid grid-cols-2 md:grid-cols-6 gap-6">
            <div v-for="(amenitie, index) in Amenities" :key="index"
                class="bg-white rounded-xl shadow p-4 flex flex-col items-center text-center">
                <img :src="amenitie.logo" :alt="amenitie.name" class="w-16 h-16 object-contain" />
                <p class="mt-2 text-sm font-bold">{{ amenitie.name }}</p>
            </div>
        </div>
    </div>
</template>

<script setup>
const Amenities = [
    { name: "24/7 Security", logo: new URL("../assets/images/Amenities/image1.png", import.meta.url).href },
    { name: "Swimming Pool", logo: new URL("../assets/images/Amenities/image2.png", import.meta.url).href },
    { name: "Kid's Play Area", logo: new URL("../assets/images/Amenities/image3.png", import.meta.url).href },
    { name: "Gymnasium", logo: new URL("../assets/images/Amenities/image4.png", import.meta.url).href },
    { name: "Car Parking", logo: new URL("../assets/images/Amenities/image5.png", import.meta.url).href },
    { name: "Jogging Track", logo: new URL("../assets/images/Amenities/image6.png", import.meta.url).href },
    { name: "Elevator", logo: new URL("../assets/images/Amenities/image7.png", import.meta.url).href },
    { name: "Indoor Games", logo: new URL("../assets/images/Amenities/image8.png", import.meta.url).href },
    { name: "Vasthu Compliant", logo: new URL("../assets/images/Amenities/image9.png", import.meta.url).href },
    { name: "Power Backup", logo: new URL("../assets/images/Amenities/image10.png", import.meta.url).href },
    { name: "Garden", logo: new URL("../assets/images/Amenities/image11.png", import.meta.url).href },
    { name: "Rainwater Harvest", logo: new URL("../assets/images/Amenities/image12.png", import.meta.url).href }
];
</script>
