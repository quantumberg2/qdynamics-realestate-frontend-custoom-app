<template>
    <header class="absolute top-0 left-0 w-full z-50 bg-transprent">
        <div class="max-w-7xl mx-auto">
            <nav class="flex items-center justify-between px-[30px] sm:px-[150px]  relative">
                <!-- Logo -->
                <div class="flex items-center space-x-2 ">
                    <router-link to="/">
                        <img src="../assets/images/DP_Logo.png" alt="Logo" class="h-12" />
                    </router-link>
                </div>

                <!-- Desktop Navigation -->
                <div
                    class="hidden md:flex items-center justify-between flex-grow font-regular mt-2 ml-4 cursor-pointer">

                    <!-- Left nav links -->
                    <ul class="flex items-center space-x-8">
                        <!-- Example for Desktop Navigation -->
                        <li>
                            <router-link to="/" class="text-gray-800 no-underline">
                                Home
                            </router-link>
                        </li>

                        <li class="relative group">
                            <div class="text-gray-800 no-underline flex items-center">
                                <router-link to="/listing" class="text-gray-800 no-underline">
                                    Listing
                                </router-link>

                                <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" viewBox="0 0 20 20"
                                    fill="currentColor">
                                    <path fill-rule="evenodd"
                                        d="M5.22 8.22a.75.75 0 0 1 1.06 0L10 11.94l3.72-3.72a.75.75 0 1 1 1.06 1.06l-4.25 4.25a.75.75 0 0 1-1.06 0L5.22 9.28a.75.75 0 0 1 0-1.06Z"
                                        clip-rule="evenodd" />
                                </svg>
                            </div>

                            <ul class="absolute hidden group-hover:block bg-white border rounded shadow-md w-60 z-50">
                                <li>
                                    <router-link :to="{ path: '/listing', query: { status: 'New' } }"
                                        class="block py-2 px-4 text-gray-800 no-underline hover:bg-gray-100">
                                        New Listing
                                    </router-link>
                                </li>

                                <li>
                                    <router-link :to="{ path: '/listing', query: { status: 'Sold Out' } }"
                                        class="block py-2 px-4 text-gray-800 no-underline hover:bg-gray-100">
                                        Completed Listing
                                    </router-link>
                                </li>
                            </ul>
                        </li>

                        <li>
                            <router-link to="/about-us" class="text-gray-800 no-underline">
                                About Us
                            </router-link>
                        </li>

                        <li class="relative group">
                            <div class="text-gray-800 no-underline flex items-center space-x-2">
                                Services
                                <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" viewBox="0 0 20 20"
                                    fill="currentColor">
                                    <path fill-rule="evenodd"
                                        d="M5.22 8.22a.75.75 0 0 1 1.06 0L10 11.94l3.72-3.72a.75.75 0 1 1 1.06 1.06l-4.25 4.25a.75.75 0 0 1-1.06 0L5.22 9.28a.75.75 0 0 1 0-1.06Z"
                                        clip-rule="evenodd" />
                                </svg>
                            </div>
                            <ul class="absolute hidden group-hover:block bg-white border rounded shadow-md w-40 z-50">
                                <li>
                                    <router-link to="/construction" class="block py-2 text-gray-800 no-underline">
                                        Construction
                                    </router-link>
                                </li>
                                <li>
                                    <router-link to="/interiors" class="block py-2 text-gray-800 no-underline">
                                        Interiors
                                    </router-link>
                                </li>
                            </ul>
                        </li>

                        <li>
                            <router-link to="/contact-us" class="block py-2 text-gray-800 no-underline">
                                Contact
                            </router-link>
                        </li>
                    </ul>

                    <!-- Right nav icons -->
                    <ul class="flex items-center space-x-4 ml-auto">
                        <li class="flex items-center space-x-2">
                            <a href="tel:+919686450917"
                                class="flex items-center space-x-2 no-underline hover:no-underline text-inherit">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                                    stroke-width="1.5" stroke="currentColor" class="w-5 h-5">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M2.25 6.75c0 8.284 6.716 15 15 15h2.25a2.25 2.25 0 0 0 2.25-2.25v-1.372c0-.516-.351-.966-.852-1.091l-4.423-1.106c-.44-.11-.902.055-1.173.417l-.97 1.293c-.282.376-.769.542-1.21.38a12.035 12.035 0 0 1-7.143-7.143c-.162-.441.004-.928.38-1.21l1.293-.97c.363-.271.527-.734.417-1.173L6.963 3.102a1.125 1.125 0 0 0-1.091-.852H4.5A2.25 2.25 0 0 0 2.25 4.5v2.25Z" />
                                </svg>
                                <span>+91 96864 50917</span>
                            </a>
                        </li>

                        <li class="relative" ref="userMenu">
                            <button @click.stop="toggleUserDropdown"
                                class="w-8 h-8 rounded-full flex items-center justify-center">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1"
                                    stroke="currentColor" class="w-5 h-5">
                                    <path stroke-linecap="round" stroke-linejoin="round"
                                        d="M17.982 18.725A7.488 7.488 0 0 0 12 15.75a7.488 7.488 0 0 0-5.982 2.975m11.963 0a9 9 0 1 0-11.963 0m11.963 0A8.966 8.966 0 0 1 12 21a8.966 8.966 0 0 1-5.982-2.275M15 9.75a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
                                </svg>
                            </button>

                            <transition name="fade-slide">
                                <ul v-if="isUserDropdownOpen"
                                    class="absolute right-0 mt-2 bg-white w-40 shadow-lg rounded-md py-2 font-regular z-50">

                                    <!-- Login / Logout -->
                                    <li v-if="!isLoggedIn">
                                        <button @click="goToLogin"
                                            class="px-2 py-2 text-gray-800 hover:bg-gray-100 no-underline text-sm w-full text-left">
                                            Login
                                        </button>
                                    </li>

                                    <li v-if="isLoggedIn">
                                        <button @click="logout"
                                            class="w-full text-left px-2 py-2 text-gray-800 hover:bg-gray-100 no-underline text-sm">
                                            Logout
                                        </button>
                                    </li>

                                    <!-- Always visible -->
                                    <li v-if="isLoggedIn">
                                        <button @click="goToDesk"
                                            class="px-2 py-2 text-gray-800 hover:bg-gray-100 no-underline text-sm w-full text-left">
                                            Switch To Desk
                                        </button>
                                    </li>
                                </ul>
                            </transition>
                        </li>
                    </ul>

                </div>

                <!-- Mobile Toggle + Menu Wrapper -->
                <div class="md:hidden relative" ref="menuWrapper">
                    <button @click.stop="toggleMenu">
                        <svg class="h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path v-if="!isOpen" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M4 6h16M4 12h16M4 18h16" />
                            <path v-else stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M6 18L18 6M6 6l12 12" />
                        </svg>
                    </button>

                    <!-- Mobile Menu -->
                    <transition name="fade-slide">
                        <ul v-if="isOpen" ref="mobileMenu"
                            class="absolute right-0 mt-2 bg-white w-60 shadow-lg rounded-md px-6 py-4 space-y-2 font-regular z-50">
                            <!-- Home -->
                            <router-link to="/" class="block font-medium text-gray-800 no-underline"
                                @click="closeMobileMenu">
                                Home
                            </router-link>

                            <!-- Listing Dropdown -->
                            <li>
                                <button @click="toggleListing"
                                    class="w-full flex justify-between items-center font-medium text-gray-800 no-underline ">
                                    <router-link to="/listing" class="text-gray-800 no-underline"
                                        @click="closeMobileMenu">
                                        Listing
                                    </router-link>
                                    <span :class="{ 'rotate-180': isListingOpen }" class="transition">
                                        <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" viewBox="0 0 20 20"
                                            fill="currentColor">
                                            <path fill-rule="evenodd"
                                                d="M5.22 8.22a.75.75 0 0 1 1.06 0L10 11.94l3.72-3.72a.75.75 0 1 1 1.06 1.06l-4.25 4.25a.75.75 0 0 1-1.06 0L5.22 9.28a.75.75 0 0 1 0-1.06Z"
                                                clip-rule="evenodd" />
                                        </svg>
                                    </span>
                                </button>

                                <ul v-show="isListingOpen" class="mt-2 space-y-2">
                                    <router-link :to="{ path: '/listing', query: { status: 'New' } }"
                                        class="block text-gray-800 no-underline" @click="closeMobileMenu">
                                        New Listing
                                    </router-link>
                                    <li>
                                        <router-link :to="{ path: '/listing', query: { status: 'Sold Out' } }"
                                            class="block text-gray-800 no-underline" @click="closeMobileMenu">
                                            Completed Listing
                                        </router-link>
                                    </li>
                                </ul>
                            </li>

                            <!-- About -->
                            <li>
                                <router-link to="/about-us" class="block font-medium text-gray-800 no-underline"
                                    @click="closeMobileMenu">
                                    About Us
                                </router-link>
                            </li>

                            <!-- Services Dropdown -->
                            <li>
                                <button @click="toggleServices"
                                    class="w-full flex justify-between items-center font-medium text-gray-800 no-underline">
                                    Services
                                    <span :class="{ 'rotate-180': isServicesOpen }" class="transition">
                                        <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" viewBox="0 0 20 20"
                                            fill="currentColor">
                                            <path fill-rule="evenodd"
                                                d="M5.22 8.22a.75.75 0 0 1 1.06 0L10 11.94l3.72-3.72a.75.75 0 1 1 1.06 1.06l-4.25 4.25a.75.75 0 0 1-1.06 0L5.22 9.28a.75.75 0 0 1 0-1.06Z"
                                                clip-rule="evenodd" />
                                        </svg>
                                    </span>
                                </button>

                                <ul v-show="isServicesOpen" class="mt-2 space-y-2">
                                    <li>
                                        <router-link to="/construction"
                                            class="block text-gray-700 text-gray-800 no-underline"
                                            @click="closeMobileMenu">
                                            Construction
                                        </router-link>
                                    </li>
                                    <li>
                                        <router-link to="/interiors" class="block text-gray-800 no-underline"
                                            @click="closeMobileMenu">
                                            Interiors
                                        </router-link>
                                    </li>
                                </ul>
                            </li>

                            <!-- Contact -->
                            <li>
                                <router-link to="/contact-us" class="block font-medium text-gray-800 no-underline"
                                    @click="closeMobileMenu">
                                    Contact
                                </router-link>
                            </li>

                            <li class="flex items-center space-x-2">
                                <a href="tel:+919686450917"
                                    class="flex items-center space-x-2 no-underline hover:no-underline text-inherit">
                                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                                        stroke-width="1.5" stroke="currentColor" class="w-5 h-5">
                                        <path stroke-linecap="round" stroke-linejoin="round"
                                            d="M2.25 6.75c0 8.284 6.716 15 15 15h2.25a2.25 2.25 0 0 0 2.25-2.25v-1.372c0-.516-.351-.966-.852-1.091l-4.423-1.106c-.44-.11-.902.055-1.173.417l-.97 1.293c-.282.376-.769.542-1.21.38a12.035 12.035 0 0 1-7.143-7.143c-.162-.441.004-.928.38-1.21l1.293-.97c.363-.271.527-.734.417-1.173L6.963 3.102a1.125 1.125 0 0 0-1.091-.852H4.5A2.25 2.25 0 0 0 2.25 4.5v2.25Z" />
                                    </svg>
                                    <span>+91 96864 50917</span>
                                </a>
                            </li>

                            <li class="relative" ref="userMenu">
                                <button @click.stop="toggleUserDropdown"
                                    class="w-8 h-8 rounded-full flex items-center justify-center">
                                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                                        stroke-width="1" stroke="currentColor" class="w-5 h-5">
                                        <path stroke-linecap="round" stroke-linejoin="round"
                                            d="M17.982 18.725A7.488 7.488 0 0 0 12 15.75a7.488 7.488 0 0 0-5.982 2.975m11.963 0a9 9 0 1 0-11.963 0m11.963 0A8.966 8.966 0 0 1 12 21a8.966 8.966 0 0 1-5.982-2.275M15 9.75a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" />
                                    </svg>
                                </button>

                                <transition name="fade-slide">
                                    <ul v-if="isUserDropdownOpen"
                                        class="absolute right-0 mt-2 bg-white w-40 shadow-lg rounded-md py-2 font-regular z-50">

                                        <!-- Login / Logout -->
                                        <li v-if="!isLoggedIn">
                                            <button @click="goToLogin"
                                                class="px-2 py-2 text-gray-800 hover:bg-gray-100 no-underline text-sm w-full text-left">
                                                Login
                                            </button>
                                        </li>

                                        <li v-if="isLoggedIn">
                                            <button @click="logout"
                                                class="w-full text-left px-2 py-2 text-gray-800 hover:bg-gray-100 no-underline text-sm">
                                                Logout
                                            </button>
                                        </li>

                                        <!-- Always visible -->
                                        <li>
                                            <button @click="goToDesk"
                                                class="px-2 py-2 text-gray-800 hover:bg-gray-100 no-underline text-sm w-full text-left">
                                                Switch To Desk
                                            </button>
                                        </li>
                                    </ul>
                                </transition>
                            </li>
                        </ul>
                    </transition>
                </div>
            </nav>
        </div>
    </header>
</template>

<script setup>
import { ref, computed, onMounted, onBeforeUnmount } from 'vue'

// ---------------- Mobile Menu ----------------
const isOpen = ref(false)
const menuWrapper = ref(null)

const isListingOpen = ref(false)
const isServicesOpen = ref(false)

// ---------------- User / Auth ----------------
const isUserDropdownOpen = ref(false)
const isLoggedIn = ref(false)
const full_name = ref('')
const userMenu = ref(null)

const closeMobileMenu = () => {
    isOpen.value = false
    isListingOpen.value = false
    isServicesOpen.value = false
    isUserDropdownOpen.value = false
}

const toggleListing = () => {
    isListingOpen.value = !isListingOpen.value
}

const toggleServices = () => {
    isServicesOpen.value = !isServicesOpen.value
}

const toggleMenu = () => {
    isOpen.value = !isOpen.value
}

const handleClickOutsideMobile = (event) => {
    if (isOpen.value && menuWrapper.value && !menuWrapper.value.contains(event.target)) {
        isOpen.value = false
    }
}

const userInitial = computed(() => {
    const name = (full_name.value || '').trim()
    return name ? name[0].toUpperCase() : ''
})

const toggleUserDropdown = () => {
    isUserDropdownOpen.value = !isUserDropdownOpen.value
}

const handleClickOutside = (event) => {
    if (isUserDropdownOpen.value && userMenu.value && !userMenu.value.contains(event.target)) {
        isUserDropdownOpen.value = false
    }
}

const getCookie = (name) => {
    const match = document.cookie.split('; ').find(row => row.startsWith(name + '='))
    return match ? decodeURIComponent(match.split('=')[1]) : ''
}

const checkLoginStatus = async () => {
    try {
        const res = await fetch('/api/method/frappe.auth.get_logged_user', { credentials: 'include' })
        const data = await res.json()

        if (data?.message && data.message !== 'Guest') {
            isLoggedIn.value = true
            full_name.value = getCookie('full_name') || data.message
        } else {
            isLoggedIn.value = false
            full_name.value = ''
        }
    } catch {
        isLoggedIn.value = false
        full_name.value = ''
    }
}

const logout = async () => {
    await fetch('/api/method/logout', { credentials: 'include' })
    isLoggedIn.value = false
    full_name.value = ''
    isUserDropdownOpen.value = false
}

const goToLogin = () => {
    window.location.assign('/login#login')
}

const goToDesk = () => {
    window.location.assign('/app/home')
}

// ---------------- Lifecycle ----------------
onMounted(() => {
    checkLoginStatus()
    document.addEventListener('click', handleClickOutside)
    document.addEventListener('click', handleClickOutsideMobile)
})

onBeforeUnmount(() => {
    document.removeEventListener('click', handleClickOutside)
    document.removeEventListener('click', handleClickOutsideMobile)
})
</script>

<style scoped>
.fade-slide-enter-active,
.fade-slide-leave-active {
    transition: all 0.2s ease;
}

.fade-slide-enter-from,
.fade-slide-leave-to {
    opacity: 0;
    transform: translateY(-5px);
}
</style>
