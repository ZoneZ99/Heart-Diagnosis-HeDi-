<template>
  <div class="container">
    <div class="card" v-for="(data, index) in news" v-bind:key="index">
      <a :href="data.url">
        <img class="img-fluid" :src="data.urlToImage" />
        <h3 class="title">{{ data.title }}</h3>
        <p class="source">{{ data.source }}</p>
      </a>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      news: []
    };
  },
  mounted() {
    axios
      .get(
        "https://newsapi.org/v2/top-headlines?country=id&category=health&apiKey=452890e5bab84a349c91a83850bfab63"
      )
      .then(response => {
        for (var data in response.data.articles) {
          var title = new String(response.data.articles[data].title);
          if (title.includes("Jantung")) {
            var newsData = {
              author: response.data.articles[data].author,
              title: response.data.articles[data].title,
              url: response.data.articles[data].url,
              urlToImage: response.data.articles[data].urlToImage,
              source: response.data.articles[data].source.name
            };
            this.news.push(newsData);
          }
        }
      })
      .catch(e => console.log(e));
  }
};
</script>

<style lang="scss" scoped>
div.container {
  width: 100%;
  padding: 2em;
  display: flex;
  overflow: scroll;

  &::-webkit-scrollbar {
    width: 0 !important;
  }

  div.card {

    box-sizing: border-box;
    border-radius: 10px;
    min-width: 250px;
    margin: 0 1em;
    padding: 20px;

    .img-fluid {
      border-radius: 10px;
      max-width: 100%;
    }

    h3 {
      margin-top: 10px;
    }

    p {
      padding-top: 10px;
      margin: 0;
      margin-block: 0;
    }

    a {
      width: 100%;
      height: 100%;
      color: black;
      text-decoration: none;
    }

    &:hover {
      box-shadow: 0px 0px 10px #ddd;

    }
  }
}
</style>