<template>
  <section class="special">
    <div class="special__top">
      <span>&lt; WEB_DEVELOPER /&gt;</span>
      <div class="special__top-status">
        <span class="special__top-status-span"></span>
        <h2 class="special__top-status-text">&lt; AVAILABLE FOR JOB /&gt;</h2>
      </div>
    </div>
    <div class="special__bottom">
      <div class="special__bottom-about">
        <h2 class="special__bottom-about-name">&lt; I’m Salokhiddin /&gt;</h2>
        <p class="special__bottom-about-descr">
          &lt; I craft excellent digital experiences through web development.
          /&gt;
        </p>
        <div class="special__bottom-about-btns">
          <div class="special__bottom-about-hire">
            <a href="mailto:guavskiy@gmail.com"
              ><button type="button" class="button__hire">
                <span class="button__hire-text">Hire Me</span>
                <span class="button__hire-icon"
                  ><svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="24"
                    viewBox="0 0 24 24"
                    stroke-width="2"
                    stroke-linejoin="round"
                    stroke-linecap="round"
                    stroke="currentColor"
                    height="24"
                    fill="none"
                    class="svg"
                  >
                    <line y2="19" y1="5" x2="12" x1="12"></line>
                    <line y2="12" y1="12" x2="19" x1="5"></line></svg
                ></span></button
            ></a>
          </div>
          <div class="special__bottom-about-copy">
            <button
              type="button"
              class="button__copy"
              @click="copyText"
              @mouseleave="normalprop"
            >
              <span class="button__copy-text">Copy Email</span>
              <span class="button__copy-icon">
                <svg
                  v-if="btnText"
                  xmlns="http://www.w3.org/2000/svg"
                  viewBox="0 0 512 512"
                >
                  <path
                    fill="#c0c0c0"
                    d="M64 464H288c8.8 0 16-7.2 16-16V384h48v64c0 35.3-28.7 64-64 64H64c-35.3 0-64-28.7-64-64V224c0-35.3 28.7-64 64-64h64v48H64c-8.8 0-16 7.2-16 16V448c0 8.8 7.2 16 16 16zM224 304H448c8.8 0 16-7.2 16-16V64c0-8.8-7.2-16-16-16H224c-8.8 0-16 7.2-16 16V288c0 8.8 7.2 16 16 16zm-64-16V64c0-35.3 28.7-64 64-64H448c35.3 0 64 28.7 64 64V288c0 35.3-28.7 64-64 64H224c-35.3 0-64-28.7-64-64z"
                  />
                </svg>
                <h2 v-else>Copied!</h2>
              </span>
            </button>
          </div>
        </div>
      </div>
      <div class="special__bottom-imgs">
        <img src="/src/assets/img/person.avif" alt="" />
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from "vue";

const btnText = ref(true);
let timeoutId;

const copyText = async () => {
  const textToCopy = "guavskiy@gmail.com";

  try {
    await navigator.clipboard.writeText(textToCopy);
    btnText.value = false; // Change the button text immediately on successful copy

    // Reset the button text after a delay (e.g., 1500 milliseconds or 1.5 seconds)
    timeoutId = setTimeout(() => {
      btnText.value = true;
    }, 1500);
  } catch (error) {
    console.error("Unable to copy text to clipboard:", error);
  }
};
const normalprop = () => {
  clearTimeout(timeoutId);
  btnText.value = true;
};
</script>
<style lang="scss" scoped></style>
