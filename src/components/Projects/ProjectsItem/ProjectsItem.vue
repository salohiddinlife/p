<template>
  <Swiper
    :modules="modules"
    :slides-per-view="1"
    :navigation="true"
    class="project__swiper"
  >
    <SwiperSlide
      class="project__slide"
      v-for="project in projects"
      :key="project.id"
    >
      <img :src="project.img" class="project__item-img" />
      <div class="project__item-info" :class="project.class">
        <h2 class="project__item-title">Title:{{ project.title }}</h2>
        <div class="project__item-descr">About:{{ project.descr }}</div>
      </div>
      <div class="project__item-link">
        <a :href="project.link"
          ><img
            class="project__item-link-img"
            src="@/assets/img/rotated_arrow.png"
            alt=""
        /></a>
        <h2 class="project__item-link-tip" :class="project.class">Click here!</h2>
      </div>
    </SwiperSlide>
  </Swiper>
</template>

<script setup>
import { Navigation } from "swiper/modules";
import { SwiperSlide, Swiper } from "swiper/vue";
import "swiper/css";
import "swiper/css/navigation";
const modules = [Navigation];
const projects = [
  {
    title: "cinephile",
    descr: "Global movie previewer",
    link: "https://gitlab.com/salokhiddin/cinephile",
    date: "Nov 25, 2023",
    img: "http://theshipninja.com/img/cinephile.png",
    class: "cinephile",
  },
  {
    title: "Todo List",
    descr:
      "Explore my Vue 3-powered to-do app—an intuitive tool demonstrating my expertise in creating responsive, user-friendly applications.",
    link: "https://salohiddinlife.github.io/todo/",
    date: "Nov 25, 2023",
    img: "http://theshipninja.com/img/todo.png",
    class: "todo",
  },
  {
    title: "vue-grocery",
    descr: "The best grocery shop in the universe",
    link: "https://gitlab.com/salokhiddin/vue-grocery",
    date: "Nov 25, 2023",
    img: "http://theshipninja.com/img/vuegrocery.png",
    class: "grocery",
  },
];
</script>

<style lang="scss" scoped></style>
