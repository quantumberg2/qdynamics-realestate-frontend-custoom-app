<template>
  <div>
    <Navbar />
    <!-- Add top padding to account for navbar height -->
    <div>
      <router-view />
    </div>

    <!-- Floating WhatsApp Button -->
    <a href="https://wa.me/919686450917" target="_blank" rel="noopener noreferrer"
      class="hidden md:block fixed bottom-20 right-5 z-50">
      <img src="./assets/images/WhatsApp.png" alt="WhatsApp"
        class="w-10 rounded-full shadow-lg hover:scale-110 transition-transform duration-300" />
    </a>

    <Scrolltotop />
    <FooterSection />
  </div>
</template>

<script setup>
import Navbar from './pages/Navbar.vue'
import FooterSection from './pages/FooterSection.vue'
import Scrolltotop from './Scrolltotop.vue'
</script>

<style>
@import "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.css";

* {
  font-family: "Roboto", sans-serif;
}
</style>
