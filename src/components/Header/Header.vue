<template>
  <header class="header">
    <div class="container">
      <div class="header__logo">
        <a href="#about" style="border: none" class="header__logo-img"
          ><img src="/src/assets/img/logo.svg" alt=""
        /></a>
      </div>
      <nav class="header__nav">
        <ul v-if="isPhoneView" class="header__nav-list">
          <a href="#about" class="header__nav-link">&lt;  About /&gt;</a> 
          <a href="#portfolio" class="header__nav-link"
            >&lt; Portfolio /&gt;</a
          >
          <a href="#contact" class="header__nav-link"
            >&lt; Contact /&gt;</a
          >
        </ul>
        <div v-else @click="burgerClick" class="sidebar_toggler">
          <span></span>
          <span></span>
          <span></span>
        </div>
          <Burger v-show="burgerClicked"/>
      </nav>
    </div>
  </header>
</template>

<script setup>
import { useWindowSize } from "vue-window-size";
import { ref, watchEffect } from "vue";
import Burger from "../Burger/Burger.vue"

const { width } = useWindowSize();
let isPhoneView;
let burgerClicked = false;
const widthRef = ref(useWindowSize().width);
function burgerClick(){
 burgerClicked = true
 return{ burgerClicked }
}

watchEffect(() => {
  isPhoneView = widthRef.value >= 600;
});

console.log("isPhoneView:", isPhoneView);
</script>

<style lang="scss" scoped>
.router-link-active {
  color: #f35034;
  text-align: center;
  font-family: "inter";
  font-size: 20px;
  font-weight: 700;
  line-height: 1.2;
  text-transform: uppercase;
  transition: 0.2s;
  border-bottom: 1px solid #f35034;
}
</style>
