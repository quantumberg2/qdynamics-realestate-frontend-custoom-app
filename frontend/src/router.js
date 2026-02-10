import { createRouter, createWebHistory } from 'vue-router'
import Listing from './pages/Listing.vue'
import Home from './pages/Home.vue'
import AboutUs from './pages/AboutUs.vue'
import Construction from './pages/Construction.vue'
import Interiors from './pages/Interiors.vue'
import ListingDetails from './pages/ListingDetails.vue'
import ContactUs from './pages/ContactUs.vue'
import PrivacyPolicy from './pages/PrivacyPolicy.vue'
import TermsAndConditions from './pages/TermsAndConditions.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/listing',
    name: 'Listing',
    component: Listing,
  },
  {
    path: '/about-us',
    name: 'AboutUs',
    component: AboutUs,
  },
  {
    path: '/construction',
    name: 'Construction',
    component: Construction,
  },
  {
    path: '/interiors',
    name: 'Interiors',
    component: Interiors,
  },
  {
    path: '/listing/:slug',
    name: 'ListingDetails',
    component: ListingDetails,
    props: true
  },
  {
    path: '/contact-us',
    name: 'ContactUs',
    component: ContactUs,
  },
  {
    path: '/privacy-policy',
    name: 'PrivacyPolicy',
    component: PrivacyPolicy,
  },
  {
    path: '/terms-and-conditions',
    name: 'TermsAndConditions',
    component: TermsAndConditions,
  },
]

const router = createRouter({
  history: createWebHistory(), // 👈 simplified
  routes,
  scrollBehavior() {
    return { top: 0 }
  }
})

export default router
