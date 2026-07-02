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
import gallery from './pages/gallery.vue'
import GalleryPage from './pages/GalleryPage.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    meta: {
      title: 'Destiny Promoters | Best Real Estate Company in Bengaluru',
      description:
        'Destiny Promoters is one of the trusted real estate companies in Bengaluru offering premium residential plots, villas, apartments, construction, and interior services.',
      keywords:
        'Destiny Promoters, Bengaluru Real Estate, Residential Plots, Villas, Apartments, Construction, Interiors'
    }
  },
  {
    path: '/listing',
    name: 'Listing',
    component: Listing,
    meta: {
      title: 'Property Listings | Destiny Promoters',
      description:
        'Explore the latest residential and commercial properties from Destiny Promoters in Bengaluru.',
      keywords:
        'Property Listings, Bengaluru Properties, Residential Plots, Villas, Apartments'
    }
  },
  {
    path: '/about-us',
    name: 'AboutUs',
    component: AboutUs,
    meta: {
      title: 'About Us | Destiny Promoters',
      description:
        'Learn about Destiny Promoters, our mission, vision, and commitment to delivering quality real estate projects.',
      keywords:
        'About Destiny Promoters, Bengaluru Builders, Real Estate Company'
    }
  },
  {
    path: '/gallery',
    name: 'gallery',
    component: gallery,
    meta: {
      title: 'Gallery | Destiny Promoters',
      description:
        'Browse our gallery showcasing completed and ongoing projects by Destiny Promoters.',
      keywords:
        'Destiny Promoters Gallery, Project Gallery, Construction Gallery'
    }
  },
  {
    path: '/gallery-page',
    name: 'GalleryPage',
    component: GalleryPage,
    meta: {
      title: 'Project Gallery | Destiny Promoters',
      description:
        'Explore photos and highlights of our residential and commercial projects.',
      keywords:
        'Project Gallery, Bengaluru Projects, Destiny Promoters'
    }
  },
  {
    path: '/construction',
    name: 'Construction',
    component: Construction,
    meta: {
      title: 'Construction Services | Destiny Promoters',
      description:
        'Professional residential and commercial construction services by Destiny Promoters.',
      keywords:
        'Construction Services, Home Construction, Building Contractors, Bengaluru'
    }
  },
  {
    path: '/interiors',
    name: 'Interiors',
    component: Interiors,
    meta: {
      title: 'Interior Design Services | Destiny Promoters',
      description:
        'Modern and customized interior design solutions for homes, apartments, and offices.',
      keywords:
        'Interior Design, Home Interiors, Office Interiors, Bengaluru'
    }
  },
  {
    path: '/listing/:slug',
    name: 'ListingDetails',
    component: ListingDetails,
    props: true,
    meta: {
      title: 'Property Details | Destiny Promoters',
      description:
        'View complete details about this property offered by Destiny Promoters.',
      keywords:
        'Property Details, Bengaluru Property, Real Estate'
    }
  },
  {
    path: '/contact-us',
    name: 'ContactUs',
    component: ContactUs,
    meta: {
      title: 'Contact Us | Destiny Promoters',
      description:
        'Contact Destiny Promoters for property enquiries, construction services, and interior design.',
      keywords:
        'Contact Destiny Promoters, Bengaluru Real Estate Contact'
    }
  },
  {
    path: '/privacy-policy',
    name: 'PrivacyPolicy',
    component: PrivacyPolicy,
    meta: {
      title: 'Privacy Policy | Destiny Promoters',
      description:
        'Read the privacy policy of Destiny Promoters regarding the collection and use of personal information.',
      keywords:
        'Privacy Policy, Destiny Promoters'
    }
  },
  {
    path: '/terms-and-conditions',
    name: 'TermsAndConditions',
    component: TermsAndConditions,
    meta: {
      title: 'Terms and Conditions | Destiny Promoters',
      description:
        'Read the terms and conditions governing the use of the Destiny Promoters website.',
      keywords:
        'Terms and Conditions, Destiny Promoters'
    }
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior() {
    return { top: 0 }
  }
})

// Function to update or create meta tags
function updateMetaTag(name, content) {
  let element = document.querySelector(`meta[name="${name}"]`)

  if (!element) {
    element = document.createElement('meta')
    element.setAttribute('name', name)
    document.head.appendChild(element)
  }

  element.setAttribute('content', content || '')
}

// Update SEO after every route change
router.afterEach((to) => {
  document.title = to.meta.title || 'Destiny Promoters'

  updateMetaTag('description', to.meta.description)
  updateMetaTag('keywords', to.meta.keywords)

  // Robots
  updateMetaTag('robots', 'index, follow')

  // Author
  updateMetaTag('author', 'Destiny Promoters')

  // Canonical URL
  let canonical = document.querySelector("link[rel='canonical']")

  if (!canonical) {
    canonical = document.createElement('link')
    canonical.setAttribute('rel', 'canonical')
    document.head.appendChild(canonical)
  }

  canonical.setAttribute(
    'href',
    window.location.origin + to.fullPath
  )

  // Open Graph Tags
  const setOGTag = (property, content) => {
    let tag = document.querySelector(`meta[property="${property}"]`)

    if (!tag) {
      tag = document.createElement('meta')
      tag.setAttribute('property', property)
      document.head.appendChild(tag)
    }

    tag.setAttribute('content', content || '')
  }

  setOGTag('og:title', to.meta.title)
  setOGTag('og:description', to.meta.description)
  setOGTag('og:type', 'website')
  setOGTag('og:url', window.location.href)
  setOGTag('og:site_name', 'Destiny Promoters')

  // Twitter Tags
  const setTwitterTag = (name, content) => {
    let tag = document.querySelector(`meta[name="${name}"]`)

    if (!tag) {
      tag = document.createElement('meta')
      tag.setAttribute('name', name)
      document.head.appendChild(tag)
    }

    tag.setAttribute('content', content || '')
  }

  setTwitterTag('twitter:card', 'summary_large_image')
  setTwitterTag('twitter:title', to.meta.title)
  setTwitterTag('twitter:description', to.meta.description)
})

export default router