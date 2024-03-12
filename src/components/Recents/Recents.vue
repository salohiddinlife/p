<template>
  <section class="recents">
    <div class="recents__title">
      <span></span>
      <h2>Recent Work</h2>
    </div>
    <div class="recents__works">
      <ul class="recents__works-list">
        <li
          v-for="(work, index) in worksList"
          :key="index"
          class="recents__works-link"
        >
          <div class="recents__works-data">
            <h2>{{ work.title }}</h2>
            <p>{{ work.date }}</p>
          </div>
          <div class="recents__works-place">
            <p>{{ work.place }}</p>
          </div>
        </li>
      </ul>
    </div>
  </section>
</template>

<script setup>
const worksList = [
  { title: "Freelancer", date: "2023 - Present", place: "UpWork" },
  { title: "Freelancer", date: "2021 - 2022", place: "Freelancer" },
  { title: "Freelancer", date: "2023 - Present", place: "Kwork" },
  { title: "Freelancer", date: "2023 - Present", place: "Fiverr" },
];
</script>

<style lang="scss" scoped></style>
