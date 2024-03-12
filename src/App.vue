<template>
  <div class="wrapper">
    <div class="container">
      <ThreeBG v-if="three"/>
    <Header />
    <Main />
    <Footer />  
    </div>
  </div>
</template>

<script setup>
import {onMounted} from 'vue'
import Header from "@/components/Header/Header.vue";
import Main from "@/components/Main/Main.vue";
import Footer from "@/components/Footer/Footer.vue";
import ThreeBG from "@/components/Three/ThreeBG.vue";

const three = false


const setScrollVar = ()=>{
  const htmlElement = document.documentElement
  const percentOfScreenHeightScrolled = htmlElement.scrollTop / htmlElement.clientHeight
  console.log(Math.min(percentOfScreenHeightScrolled * 100,100));
  htmlElement.style.setProperty("--scroll", Math.min(percentOfScreenHeightScrolled * 100,100))
}
window.addEventListener("scroll",setScrollVar)
window.addEventListener("resize",setScrollVar)
onMounted(() => {
  setScrollVar()
})
</script>

<style lang="scss" scoped></style>
