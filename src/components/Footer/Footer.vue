<template>
  <footer class="footer" id="contact">
    <div class="container">
      <div class="footer__content">
        <h2 class="footer__title">Portfolio 2024</h2>
        <ul class="footer__list">
          <li v-for="link in links" :key="link.id" >
            <a :href="link.link" class="footer__link">{{ link.title }}</a>
          </li>
        </ul>
        <div class="special__top-status">
          <span class="special__top-status-span"></span>
          <h2 class="special__top-status-text">&lt; AVAILABLE FOR JOB /&gt;</h2>
        </div>
      </div>
    </div>
  </footer>
</template>

<script setup>
const links = [
  {
    title: "Instagram",
    link: "https://www.instagram.com/soloha.coder?igsh=MTVoMWhldWNlNGhvNA==",
  },
  {
    title: "LinkedIn",
    link: "https://www.linkedin.com/in/salokhiddin-khairiddinov-a7b4a1277",
  },
  {
    title: "X/Twitter",
    link: "https://x.com/SolohaC?s=35",
  },
  {
    title:"Telegram",
    link:"https://t.me/gangster_stuff"
  }
];
</script>

<style lang="scss" scoped></style>
