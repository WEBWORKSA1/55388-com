/* 55388.com — site configuration. Edit values here; no page needs to change. */
window.SITE_CONFIG = {
  siteName: "55388",
  siteUrl: "https://55388.com",
  // External interest link shown in the top banner of every page
  interestUrl: "https://web.works/contact",

  // Contact routing: stored encoded, assembled only at submit/click time. Never paste a plain address anywhere in the site.
  _k: ["=02bj", "5CbpF", "WbnBU", "MhN3a", "y92di", "V2d"],
  // Optional: after activating FormSubmit, paste the random alias it emails you (e.g. "a1b2c3d4e5...") to stop using the encoded address.
  formAlias: "",

  // Google AdSense — set your publisher ID (ca-pub-XXXXXXXXXXXXXXXX) to switch every ad slot on.
  adsenseClient: "",
  adsenseSlots: { header: "", inArticle: "", sidebar: "", footer: "" },

  // Google Analytics 4 measurement ID (G-XXXXXXX). Loaded only after consent.
  ga4: "",

  // Monetization links — leave blank to fall back to the on-site forms.
  donateLinks: { paypal: "", kofi: "", buymeacoffee: "", stripe: "" },
  affiliate: {
    liveReading: "",   // e.g. your Keen / Kasamba / Psychic Source affiliate link
    fullReport: "",    // e.g. your ClickBank numerology report hop-link
    shop: ""           // e.g. Amazon storefront for number jewelry & books
  },
  youtubeChannel: "",  // your own channel URL; shows a Subscribe button when set
  newsletterAction: "" // optional ESP form action (Mailchimp/ConvertKit). Blank = email to inbox.
};
