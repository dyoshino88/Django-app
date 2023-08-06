/** @type {import('tailwindcss').Config} */
module.exports = {
  future: {
    removeDeprecatedGapUtilities: true,
    purgeLayersByDefault: true,
  },
  purge: {
    enabled: false,
    content: ['../bulletinboard/templates/base.html', '../bulletinboard/templates/accounts/registration.html'],
  },
  theme: {
    extend: {},
  },
  variants: {},
  plugins: [],
}