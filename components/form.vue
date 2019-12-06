<template>
  <client-only>
    <full-page ref="fullpage" :options="options" id="fullpage">
      <div id="form-diagnosa">
        <form method="post">
          <div class="section">
            <div class="center">
              <div class="form-group">
                <label for="namaPanjang">Siapa nama kamu ? *</label>
                <div>
                  <input
                    placeholder="Tulis nama kamu disini..."
                    v-model="form['nama']"
                    id="namaPanjang"
                    type="text"
                    class="input-text"
                    required
                  />
                </div>
                <button
                  class="next btn out-green"
                  @click="$refs.fullpage.api.moveSectionDown()"
                >
                  Next
                </button>
              </div>
            </div>
          </div>

          <div id="jenisKelaminPage" class="section">
            <div class="center">
              <div class="form-group">
                <label for="jenisKelamin">Jenis Kelamin Kamu,____? *</label>
                <div>
                  <select
                    name="gender"
                    v-model="form['jenisKelamin']"
                    id="jenisKelamin"
                    aria-placeholder="Pilih Jenis Kelamin . . ."
                    class="input-text"
                  >
                    <option value>Pilih Jenis Kelamin...</option>
                    <option value="1">Perempuan</option>
                    <option value="2">Laki-Laki</option>
                  </select>
                </div>
                <div class="flex">
                  <button
                    class="next btn cancel"
                    @click="$refs.fullpage.api.moveSectionUp()"
                  >
                    Previous
                  </button>
                  <button
                    class="next btn out-green"
                    @click="$refs.fullpage.api.moveSectionDown()"
                  >
                    Next
                  </button>
                </div>
              </div>
            </div>
          </div>

          <div class="section">
            <div class="center">
              <div class="form-group">
                <label for="tglLahir">Tanggal Lahir</label>
                <div class="row">
                  <input
                    id="tglLahir"
                    v-model="form['tanggalLahir']"
                    type="date"
                    class="input-text"
                    required
                  />
                  <p class="format">tahun</p>
                </div>
                <div class="flex">
                  <button
                    class="next btn cancel"
                    @click="$refs.fullpage.api.moveSectionUp()"
                  >
                    Previous
                  </button>
                  <button
                    class="next btn out-green"
                    @click="$refs.fullpage.api.moveSectionDown()"
                  >
                    Next
                  </button>
                </div>
              </div>
            </div>
          </div>

          <div class="section">
            <div class="center">
              <div class="form-group">
                <label for="tinggiBadan">Tinggi Badan</label>
                <div class="row">
                  <input
                    id="tinggiBadan"
                    v-model="form['tinggiBadan']"
                    type="number"
                    min="0"
                    class="input-number"
                    required
                  />
                  <p class="format">cm</p>
                </div>
                <div class="flex">
                  <button
                    class="next btn cancel"
                    @click="$refs.fullpage.api.moveSectionUp()"
                  >
                    Previous
                  </button>
                  <button
                    class="next btn out-green"
                    @click="$refs.fullpage.api.moveSectionDown()"
                  >
                    Next
                  </button>
                </div>
              </div>
            </div>
          </div>

          <div class="section">
            <div class="center">
              <div class="form-group">
                <label for="berat-badan">Berat Badan</label>
                <div class="row">
                  <input
                    id="beratBadan"
                    v-model="form['beratBadan']"
                    type="number"
                    min="0"
                    class="input-number"
                    required
                  />
                  <p class="format">Kg</p>
                </div>
                <div class="flex">
                  <button
                    class="next btn cancel"
                    @click="$refs.fullpage.api.moveSectionUp()"
                  >
                    Previous
                  </button>
                  <button
                    class="next btn out-green"
                    @click="$refs.fullpage.api.moveSectionDown()"
                  >
                    Next
                  </button>
                </div>
              </div>
            </div>
          </div>

          <div class="section">
            <div class="center">
              <div class="form-group">
                <label for="tekananSistolik">Tekanan Sistolik</label>
                <div class="row">
                  <input
                    id="tekananSistolik"
                    v-model="form['tekananSistolik']"
                    type="number"
                    min="0"
                    class="input-number"
                    required
                  />
                  <p class="format">mmHg</p>
                </div>
                <div class="flex">
                  <button
                    class="next btn cancel"
                    @click="$refs.fullpage.api.moveSectionUp()"
                  >
                    Previous
                  </button>
                  <button
                    class="next btn out-green"
                    @click="$refs.fullpage.api.moveSectionDown()"
                  >
                    Next
                  </button>
                </div>
              </div>
            </div>
          </div>

          <div class="section">
            <div class="center">
              <div class="form-group">
                <label for="tekananSistolik">Tekanan Diastolik</label>
                <div class="row">
                  <input
                    id="tekananDiastolik"
                    v-model="form['tekananDiastolik']"
                    type="number"
                    min="0"
                    class="input-number"
                    required
                  />
                  <p class="format">mmHg</p>
                </div>
                <div class="flex">
                  <button
                    class="next btn cancel"
                    @click="$refs.fullpage.api.moveSectionUp()"
                  >
                    Previous
                  </button>
                  <button
                    class="next btn out-green"
                    @click="$refs.fullpage.api.moveSectionDown()"
                  >
                    Next
                  </button>
                </div>
              </div>
            </div>
          </div>

          <div class="section">
            <div class="center">
              <div class="form-group">
                <label for="tingkat-kolesterol">Tingkat Kolesterol</label>
                <div id="tingkat-kolesterol" class="btn-level-group">
                  <button
                    type="button"
                    class="btn option"
                    v-on:click="ColGood"
                    v-bind:class="{ good: isColGood }"
                  >
                    Normal (< 200)
                  </button>
                  <button
                    type="button"
                    class="btn option"
                    v-on:click="ColImportant"
                    v-bind:class="{ 'good important': isColImportant }"
                  >
                    Sedang (200-239)
                  </button>
                  <button
                    type="button option"
                    class="btn option"
                    v-on:click="ColDanger"
                    v-bind:class="{ 'good important danger': isColDanger }"
                  >
                    Tinggi (>240)
                  </button>
                </div>
                <div class="flex">
                  <button
                    class="next btn cancel"
                    @click="$refs.fullpage.api.moveSectionUp()"
                  >
                    Previous
                  </button>
                  <button
                    class="next btn out-green"
                    @click="$refs.fullpage.api.moveSectionDown()"
                  >
                    Next
                  </button>
                </div>
              </div>
            </div>
          </div>

          <div class="section">
            <div class="center">
              <div class="form-group">
                <label for="tingkat-glukosa"
                  >Tingkat Glukosa (2 jam setelah makan)</label
                >
                <div id="tingkat-glukosa" class="btn-level-group">
                  <button
                    type="button"
                    class="btn option"
                    v-on:click="GluGood"
                    v-bind:class="{ good: isGluGood }"
                  >
                    Normal (< 120)
                  </button>
                  <button
                    type="button"
                    class="btn option"
                    v-on:click="GluImportant"
                    v-bind:class="{ 'good important': isGluImportant }"
                  >
                    Sedang (140-199)
                  </button>
                  <button
                    type="button"
                    class="btn option"
                    v-on:click="GluDanger"
                    v-bind:class="{ 'good important danger': isGluDanger }"
                  >
                    Tinggi (>200)
                  </button>
                </div>
                <div class="flex">
                  <button
                    class="next btn cancel"
                    @click="$refs.fullpage.api.moveSectionUp()"
                  >
                    Previous
                  </button>
                  <button
                    class="next btn out-green"
                    @click="$refs.fullpage.api.moveSectionDown()"
                  >
                    Next
                  </button>
                </div>
              </div>
            </div>
          </div>

          <div class="section">
            <div class="center">
              <div class="form-group">
                <input
                  type="checkbox"
                  v-model="form['isOlahraga']"
                  name="olahraga"
                  id="olahraga"
                />
                <label for="olahraga">Apakah kamu sering olah raga ?</label>
              </div>
              <div class="flex">
                <button
                  class="next btn cancel"
                  @click="$refs.fullpage.api.moveSectionUp()"
                >
                  Previous
                </button>
                <button
                  class="next btn out-green"
                  @click="$refs.fullpage.api.moveSectionDown()"
                >
                  Next
                </button>
              </div>
            </div>
          </div>

          <div class="section">
            <div class="center">
              <div class="form-group">
                <input
                  type="checkbox"
                  v-model="form['isMerokok']"
                  name="perokok"
                  id="perokok"
                />
                <label for="perokok">Apakah kamu seorang perokok aktif ?</label>
              </div>
              <div class="flex">
                <button
                  class="next btn cancel"
                  @click="$refs.fullpage.api.moveSectionUp()"
                >
                  Previous
                </button>
                <button
                  class="next btn out-green"
                  @click="$refs.fullpage.api.moveSectionDown()"
                >
                  Next
                </button>
              </div>
            </div>
          </div>

          <div class="section">
            <div class="center">
              <div class="form-group">
                <input
                  type="checkbox"
                  v-model="form['isPeminum']"
                  name="peminum"
                  id="peminum"
                />
                <label for="peminum"
                  >Apakah kamu seorang pecandu alkohol ?</label
                >
              </div>
              <div class="flex">
                <button
                  class="next btn cancel"
                  @click="$refs.fullpage.api.moveSectionUp()"
                >
                  Previous
                </button>
                <button
                  class="next btn out-green"
                  @click="$refs.fullpage.api.moveSectionDown()"
                >
                  Next
                </button>
              </div>
            </div>
          </div>

          <div class="section">
            <div class="center">
              <div class="form-group">
                <div v-if="result === ''">
                  <label>Diagnosa Sekarang ?</label>
                  <div class="errorMessage" v-if="error !== ''">
                    <p>* {{ error }}</p>
                  </div>
                  <div class="flex">
                    <button
                      class="next btn cancel"
                      @click="$refs.fullpage.api.moveSectionUp()"
                    >
                      Previous
                    </button>
                    <button
                      type="submit"
                      v-on:click="submitForm"
                      class="btn success"
                    >
                      Diagnosa
                    </button>
                  </div>
                </div>

                <div class="v-flex-center" v-else-if="result !== ''">
                  <div id="result">
                    <p id="description">
                      Hasil diagnosa menunjukkan bahwa
                      <br />
                      <strong>{{ form.nama }}</strong>
                    </p>
                    <h1 class="result-str good" v-if="result === 1">
                      Terindikasi
                    </h1>
                    <h1 class="result-str bad" v-else-if="result === 0">
                      Tidak Terindikasi
                    </h1>
                    <p>
                      <strong>Penyakit Jantung</strong>
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </form>
      </div>
    </full-page>
  </client-only>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      options: {
        licenseKey: "YOUR_KEY_HERE"
      },
      form: {
        nama: "",
        jenisKelamin: "",
        tanggalLahir: "",
        beratBadan: 0,
        tinggiBadan: 0,
        tekananSistolik: 0,
        tekananDiastolik: 0,
        tingkatKolesterol: 1,
        tingkatGlukosa: 1,
        isOlahraga: false,
        isMerokok: false,
        isPeminum: false
      },
      result: "",
      isColGood: true,
      isColImportant: false,
      isColDanger: false,
      isGluGood: true,
      isGluImportant: false,
      isGluDanger: false,
      error: "",
      loading: false
    };
  },
  methods: {
    submitForm() {
      event.preventDefault();
      this.loading = true;
      if (this.form.nama == "") {
        this.error = "Isi Nama terlebih dahulu !";
      } else if (this.form.jenisKelamin == "") {
        this.error = "Isi Jenis Kelamin terlebih dahulu !";
      } else if (this.form.tanggalLahir == "") {
        this.error = "Isi Tanggal Lahir terlebih dahulu !";
      } else if (this.form.beratBadan == 0) {
        this.error = "Isi Berat Badan dengan benar !";
      } else if (this.form.tinggiBadan == 0) {
        this.error = "Isi Tinggi Badan dengan benar !";
      } else {
        axios
          .post("https://hedi-backend.herokuapp.com/result/", this.form)
          .then(response => {
            this.result = response.data.result;
          });
      }
    },
    cancelForm() {},
    ColGood() {
      if (this.isColGood) {
        this.isColGood = true;
      } else {
        this.isColGood = !this.isColGood;
      }
      this.isColDanger = false;
      this.isColImportant = false;
      this.form.tingkatKolesterol = 1;
    },
    ColImportant() {
      if (!this.isColGood) {
        this.isColGood = true;
      }
      if (this.isColImportant) {
        this.isColImportant = true;
      } else {
        this.isColImportant = !this.isColImportant;
      }
      this.isColDanger = false;
      this.form.tingkatKolesterol = 2;
    },
    ColDanger() {
      if (!this.isColImportant) {
        this.isColGood = true;
        this.isColImportant = true;
      }
      if (this.isColDanger) {
        this.isColDanger = true;
      } else {
        this.isColDanger = !this.isColDanger;
      }
      this.form.tingkatKolesterol = 3;
    },
    GluGood() {
      if (this.isGluGood) {
        this.isGluGood = true;
      } else {
        this.isGluGood = !this.isGluGood;
      }
      this.isGluDanger = false;
      this.isGluImportant = false;
      this.form.tingkatGlukosa = 1;
    },
    GluImportant() {
      if (!this.isGluGood) {
        this.isGluGood = true;
      }
      if (this.isGluImportant) {
        this.isGluImportant = true;
      } else {
        this.isGluImportant = !this.isGluImportant;
      }
      this.isGluDanger = false;
      this.form.tingkatGlukosa = 2;
    },
    GluDanger() {
      if (!this.isGluImportant) {
        this.isGluGood = true;
        this.isGluImportant = true;
      }
      if (this.isGluDanger) {
        this.isGluDanger = true;
      } else {
        this.isGluDanger = !this.isGluDanger;
        this.form.tingkatGlukosa = 3;
      }
    }
  }
};
</script>

<style lang="scss" scoped>
@media only screen and (max-width: 700px) {
  div#form-diagnosa {
    form {
      .section {
        padding: 2em !important;
      }
    }
  }
}
div#form-diagnosa {
  h1#title-form-diagnosa {
    font-size: 32px;
    padding-bottom: 1em;
  }

  form {
    p {
      margin: 0;
      margin-block: 0;
    }

    .section {
      height: 100vh;
      width: 100vw;
      padding: 0 10em;

      .center {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        justify-content: center;
      }
    }

    .form-group {
      width: 100%;

      .input-text {
        width: 100%;
        height: 3em;
      }

      .input-number {
        width: 10em;
        height: 4em;
      }

      div.btn-level-group {
        display: flex;

        .btn {
          padding: 10px;
        }
      }

      label {
        font-size: 32px;
        font-weight: bold;
      }

      div {
        margin-top: 10px;

        .btn {
          text-align: center;

          h4 {
            font-weight: 600;
          }
        }

        input {
          height: 15px;
          line-height: 15px;
        }

        input,
        select {
          background: transparent;
          border: none;
          border-bottom: 1px solid #eee;
          text-overflow: ellipsis;
          overflow: hidden;
          color: #888;
          font-size: 24px;
          font-family: "Signika", "Arial", sans-serif;
          transition: all 0.5s ease;

          &:focus {
            outline: none;
            border-bottom: 1px solid black;
          }
        }

        input.btn {
          border-radius: 0;
          height: 40px;
          padding: 10px;
        }

        p.format {
          margin-left: 10px;
        }
      }
    }
  }
}

.row {
  display: flex;
  align-items: center;
  flex-direction: row;
}

.btn {
  outline: none;
  border: none;
  padding: 8px;
  margin: 0;
  display: block;
  color: #222;
  cursor: pointer;
  background: #eee;

  &.good {
    background: #32dbc6;
  }

  &.important {
    background: #f6d365;
  }

  &.danger {
    background: #f0134d;
  }
}

h1 {
  .good {
    color: #32dbc6;
  }

  .bad {
    color: #f0134d;
  }
}

.success {
  background: #50b6bb;
  color: white;

  &:hover {
    background: #222;
    color: white;
  }
}

.cancel {
  background: #eee;
  color: #222;

  &:hover {
    background: #222;
    color: white;
  }
}

a {
  text-decoration: none;
}
.btn {
  margin-top: 20px;
  margin-right: 10px;
  border-radius: 2px;
  text-transform: uppercase;

  &.out-green {
    background: transparent;
    border: 1px solid #32dbc6;

    &:hover {
      background: #32dbc6;
    }
  }

  &.option {
    border-radius: 0;
    margin: 0;
  }
}

.v-flex-center {
  display: flex;
  align-items: center;
  justify-content: center;
}

.errorMessage {
  color: red;
  font-size: 14px;
}

div#result {
  margin: 2em;
  border: 1px solid #eee;
  border-radius: 10px;
  padding: 1em;
  text-align: center;
}

div.flex {
  display: flex;
}
</style>
