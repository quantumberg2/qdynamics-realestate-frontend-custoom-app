<template>
    <div class="fixed bottom-0 left-0 w-full bg-[#1a1a1a] border-t shadow-md z-50 md:hidden">
        <div class="grid grid-cols-3 text-center">

            <!-- Call -->
            <a href="tel:+919686450917"
                class="flex items-center justify-center gap-2 py-2 text-white border-r border-white/40">
                <i class="bi bi-telephone text-lg"></i>
                <span class="text-sm">Call</span>
            </a>

            <!-- Enquire -->
            <router-link to="/contact-us"
                class="flex items-center justify-center gap-2 py-2 text-white border-r border-white/40">
                <i class="bi bi-envelope text-lg"></i>
                <span class="text-sm">Enquire</span>
            </router-link>

            <!-- WhatsApp -->
            <a href="https://wa.me/919686450917" target="_blank"
                class="flex items-center justify-center gap-2 py-2 text-white">
                <i class="bi bi-whatsapp text-lg text-green-400"></i>
                <span class="text-sm">WhatsApp</span>
            </a>

        </div>
    </div>
</template>