<template>
  <div>
    <section id="hedi-developer">
      <h1 data-aos="fade">Men Behind The Project</h1>
      <div class="grid">
        <div class="card" data-aos="fade-right">
          <div class="circle">
            <img src="~/assets/profile-supri.jpg" alt="Ahmad Supriyanto" />
          </div>
          <h3 class="name">Ahmad Supriyanto</h3>
          <p class="description">Frontend Developer</p>
        </div>
        <div class="card" data-aos="fade-right">
          <div class="circle"></div>
          <h3 class="name">Alfian Fuadi</h3>
          <p class="description">Programmer</p>
        </div>
        <div class="card" data-aos="fade-right">
          <div class="circle">
            <img src="~/assets/profile-farhan.jpg" alt />
          </div>
          <h3 class="name">Farhan Azyumardhi</h3>
          <p class="description">Programmer</p>
        </div>
        <div class="card" data-aos="fade-right">
          <div class="circle">
            <img src="~/assets/profile-vincent.jpg" alt />
          </div>
          <h3 class="name">Vincentius Adi</h3>
          <p class="description">Programmer</p>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import AOS from "aos";
export default {
  mounted() {
    AOS.init();
  }
};
</script>

<style lang="scss" scoped>
section#hedi-developer {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 4em;

  .grid {
    margin-top: 2em;
    width: 100%;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));

    .card {
      padding: 2em;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;

      .circle {
        height: 8em;
        width: 8em;
        background: #eee;
        clip-path: circle(50% at 50% 50%);
        margin-bottom: 2em;

        img {
          max-height: 100%;
        }
      }

      p {
        margin-block: 0;
        text-align: center;
      }

      h3 {
        text-align: center;
      }
    }
  }
}

@media only screen and (min-width: 700px) {
  section#hedi-developer {
    height: 100vh;
  }
}
</style>
