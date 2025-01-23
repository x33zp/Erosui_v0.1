/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      fontFamily: {
        dmSans: ["DM sans", "sans-serif"],
        montserrat: ["montserrat", "sans-serif"],
        openSans: ["Open Sans", "sans-serif"],
        outfit: ["outfit", "sans-serif"],
      },

      colors: {
        grayLight: "#e1e1e1",
        gray: "#929292",
        primary: "#A2C48D",
        primaryDark: "#83A66E",
        light: "#FFFFFF",
        black: "#242424",
        brown: "#19110b",
      },

      backgroundImage: {
        grain: "url('./src/assets/grain.png')",
      },
    },
  },
  plugins: [],
};
