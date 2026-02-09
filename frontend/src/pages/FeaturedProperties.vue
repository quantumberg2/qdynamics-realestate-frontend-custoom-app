<template>
    <div class="container mx-auto px-4 py-8">

        <!-- Section Heading -->
        <div class="text-center mb-6">
            <div class="font-semibold text-7xl">Featured Properties</div>
            <p class="text-xs">Lorem ipsum dolor sit amet</p>
        </div>

        <!-- Cards Grid -->
        <div class="row g-4">
            <div v-for="property in properties" :key="property.id" class="col-12 col-sm-6 col-lg-3">
                <router-link v-if="property.slug" :to="{ name: 'ListingDetails', params: { slug: property.slug } }"
                    class="text-decoration-none">
                    <div class="card h-100 shadow-sm border-0 rounded-3">

                        <!-- Image Section -->
                        <div class="relative p-2 pb-0">
                            <img :src="property.image" class="card-img-top rounded-3" alt="Property" />

                            <!-- Status Badge -->
                            <div class="absolute top-6 left-6">
                                <span v-if="property.status" class="px-3 py-1 text-xs font-bold rounded-full"
                                    :class="badgeColors(property.status)">
                                    {{ property.status }}
                                </span>
                            </div>
                        </div>

                        <!-- Card Body -->
                        <div class="card-body">
                            <h6 class="text-red-400 font-semibold text-[13px]">
                                {{ property.title }}
                            </h6>

                            <div class="card-title fw-semibold mb-1 text-[13px]">
                                {{ property.subtitle }}
                            </div>

                            <div class="text-xs mb-2 d-flex align-items-center">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2"
                                    stroke="currentColor" class="h-4 w-4 me-1">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M15 10.5a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1 1 15 0Z" />
                                </svg>
                                {{ property.location }}
                            </div>

                            <!-- Features -->
                            <div class="d-flex flex-wrap gap-3 text-sm text-secondary">
                                <span class="d-flex align-items-center gap-2">
                                    <img src="../assets/images/Bed.png" alt="" class="h-3" />
                                    {{ property.beds }}
                                </span>

                                <span class="d-flex align-items-center gap-2">
                                    <img src="../assets/images/Bath.png" alt="" class="h-3" />
                                    {{ property.baths }}
                                </span>

                                <span class="d-flex align-items-center gap-2">
                                    <img src="../assets/images/Sqft.png" alt="" class="h-3" />
                                    {{ property.sizes }}
                                </span>
                            </div>
                        </div>

                    </div>
                </router-link>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from "vue"

const properties = ref([])

onMounted(async () => {
    try {
        const res = await fetch(
            "/api/method/destiny_promoters_website.api.project_api.get_projects?tag=Featured-Properties"
        )
        if (!res.ok) throw new Error("Failed to fetch featured properties")

        const data = await res.json()

        properties.value = data.message.map(p => ({
            id: p.name,                         // internal use (optional)
            slug: p.route || p.url || null,     // ✅ SEO URL
            title: p.heading_first || "Featured Property",
            subtitle: p.project_name,
            location: p.full_location,
            beds: p.bhk || "-",
            baths: p.bath || "-",
            sizes: p.super_built_up_area || "-",
            status: p.status,
            image: p.thumbnail
        }))
    } catch (err) {
        console.error("Featured properties error:", err)
    }
})

const badgeColors = (status) => {
    switch (status) {
        case "New":
            return "bg-black text-white"
        case "Sold Out":
            return "bg-black text-white"
        case "Ongoing":
            return "bg-black text-white"
        case "Coming Soon":
            return "bg-black text-white"
        default:
            return "bg-black text-white"
    }
}
</script>
