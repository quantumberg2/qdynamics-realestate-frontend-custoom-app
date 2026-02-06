<template>
    <div>
        <div class="font text-[220%] font-semibold">Send Us a Suggestion!</div>
        <div class="font-light text-xs text-gray-900 mb-3">
            Have an idea or improvements in mind? Let us know!
        </div>
        <!-- Contact Form -->
        <form @submit.prevent="submitSuggestion" class="space-y-4">
            <!-- Name -->
            <div>
                <label for="name" class="block text-xs mb-1">Your Name</label>
                <input v-model="form.name" type="text" id="name" placeholder="Enter your name"
                    class="form-control rounded-md border border-gray-400 w-full py-0 px-3 focus:outline-none focus:ring-2 focus:ring-black placeholder:text-xs" />
            </div>

            <!-- Email -->
            <div>
                <label for="email" class="block text-xs mb-1">Your Email</label>
                <input v-model="form.email" type="email" id="email" placeholder="Enter your email"
                    class="form-control rounded-md border border-gray-400 w-full py-0 px-3 focus:outline-none focus:ring-2 focus:ring-black placeholder:text-xs" />
            </div>

            <!-- Contact -->
            <div>
                <label for="contact" class="block text-xs mb-1">Your Contact Number</label>
                <input v-model="form.contact" type="text" id="contact" placeholder="Enter your contact number"
                    class="form-control rounded-md border border-gray-400 w-full py-0 px-3 focus:outline-none focus:ring-2 focus:ring-black placeholder:text-xs" />
            </div>

            <!-- Subject -->
            <div>
                <label for="subject" class="block text-xs mb-1">Your Message Subject</label>
                <input v-model="form.subject" type="text" id="subject" placeholder="Enter your message subject"
                    class="form-control rounded-md border border-gray-400 w-full py-0 px-3 focus:outline-none focus:ring-2 focus:ring-black placeholder:text-xs" />
            </div>

            <!-- Message -->
            <div>
                <label for="message" class="block text-xs mb-1">Your Message</label>
                <textarea v-model="form.message" id="message" rows="4" placeholder="Enter your message"
                    class="form-control rounded-md border border-gray-400 w-full py-2 px-3 focus:outline-none focus:ring-2 focus:ring-black placeholder:text-xs"></textarea>
            </div>

            <!-- Submit Button -->
            <div>
                <button type="submit" :disabled="loading"
                    class="w-full bg-black text-white py-2 text-sm rounded-md hover:bg-black flex items-center justify-center">
                    <span v-if="!loading">Submit</span>
                    <span v-else
                        class="ml-2 w-4 h-4 border-2 border-white border-t-transparent rounded-full animate-spin"></span>
                </button>
            </div>

            <!-- Response Message -->
            <p v-if="responseMessage" :class="responseClass" class="text-xs mt-2">
                {{ responseMessage }}
            </p>
        </form>
    </div>
</template>

<script>
export default {
    data() {
        return {
            form: {
                name: "",
                email: "",
                contact: "",
                subject: "",
                message: "",
            },
            loading: false,
            responseMessage: "",
            responseClass: "",
        };
    },
    methods: {
        async submitSuggestion() {
            this.responseMessage = "";
            this.loading = true;

            try {
                const body = new URLSearchParams(this.form);
                const res = await fetch(
                    "/api/method/destiny_promoters_website.contact_api.send_suggestion",
                    {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/x-www-form-urlencoded",
                        },
                        body,
                        credentials: "omit",
                    }
                );

                const data = await res.json();

                // Frappe wraps inside `message`
                const payload = data.message || data;

                if (res.ok && payload.status === "success") {
                    this.responseMessage = payload.message;
                    this.responseClass = "text-green-600 font-medium";

                    // ✅ clear the form
                    this.form = {
                        name: "",
                        email: "",
                        contact: "",
                        subject: "",
                        message: "",
                    };
                } else {
                    this.responseMessage = payload.message || "Something went wrong. Please try again.";
                    this.responseClass = "text-red-600 font-medium";
                }

                // Auto-hide after 3 sec
                setTimeout(() => {
                    this.responseMessage = "";
                }, 3000);

            } catch (err) {
                console.error(err);
                this.responseMessage = "Server error. Please try again later.";
                this.responseClass = "text-red-600 font-medium";
                setTimeout(() => {
                    this.responseMessage = "";
                }, 3000);
            } finally {
                this.loading = false;
            }
        },
    },
};
</script>
