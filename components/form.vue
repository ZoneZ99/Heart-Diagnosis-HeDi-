<template>
  <div id="form-diagnosa">
    <h1 id="title-form-diagnosa">Form Diagnosa Penyakit Jantung</h1>
    <form method="post">
      <div class="form-group">
        <label for="nama-panjang">Nama Panjang</label>
        <div>
          <input id="nama-panjang" type="text" />
        </div>
      </div>
      <div class="form-group">
        <label for="jenis-kelamin">Jenis Kelamin</label>
        <div>
          <select name="gender" id="jenis-kelamin" aria-placeholder="Pilih Jenis Kelamin . . .">
            <option value>Pilih Jenis Kelamin...</option>
            <option value="0">Laki-Laki</option>
            <option value="0">Perempuan</option>
          </select>
        </div>
      </div>
      <div class="form-group">
        <label for="umur">Umur</label>
        <div id="umur" class="row">
          <input type="text" />
          <p class="format">tahun</p>
        </div>
      </div>
      <div class="form-group">
        <label for="tinggi-badan">Tinggi Badan</label>
        <div id="tinggi-badan" class="row">
          <input type="text" />
          <p class="format">cm</p>
        </div>
      </div>
      <div class="form-group">
        <label for="berat-badan">Berat Badan</label>
        <div class="row">
          <input type="text" />
          <p class="format">Kg</p>
        </div>
      </div>
      <div class="form-group">
        <label for="tekanan-sistolik">Tekanan Sistolik</label>
        <div id="tekanan-sistolik" class="row">
          <input type="text" />
          <p class="format">mmHg</p>
        </div>
      </div>
      <div class="form-group">
        <label for="tingkat-kolesterol">Tingkat Kolesterol</label>
        <div id="tingkat-kolesterol" class="btn-level-group">
          <input type="button" class="btn" v-bind:class="getColGood" value="Normal (< 200)" />
          <input type="button" class="btn" v-bind:class="getColImportant" value="Sedang (200-239)" />
          <input type="button" class="btn" v-bind:class="getColDanger" value="Tinggi (>240)" />
        </div>
      </div>
      <div class="form-group">
        <label for="tingkat-glukosa">Tingkat Glukosa (2 jam setelah makan)</label>
        <div id="tingkat-glukosa" class="btn-level-group">
          <input type="button" class="btn" v-bind:class="getGluGood" value="Normal (< 120)" />
          <input type="button" class="btn" v-bind:class="getGluImportant" value="Sedang (140-199)" />
          <input type="button" class="btn" v-bind:class="getGluDanger" value="Tinggi (>200)" />
        </div>
      </div>
      <div class="form-group">
        <input type="checkbox" name="olahraga" id="olahraga" />
        <label for="olahraga">Apakah kamu sering olah raga ?</label>
      </div>
      <div class="form-group">
        <input type="checkbox" name="olahraga" id="olahraga" />
        <label for="olahraga">Apakah kamu seorang perokok aktif ?</label>
      </div>
      <div class="form-group">
        <input type="checkbox" name="olahraga" id="olahraga" />
        <label for="olahraga">Apakah kamu seorang pecandu alkohol ?</label>
      </div>
      <div id="button-group">
        <button class="btn cancel">Batal</button>
        <button type="submit" class="btn success">Diagnosa</button>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  data: {
    isColDanger: false,
    isColImportant: false,
    isColGood: false
  },
  methods: {
    getColDanger() {
      return {
        good: true,
        important: true,
        danger: this.data["isGood"]
      };
    },
    getColImportant() {
      return {
        good: true,
        important: !this.data["isImportant"]
      };
    },
    getGluGood() {
      return {
        good: true
      };
    },
    getGluDanger() {
      return {
        good: true,
        important: true,
        danger: !this.data["isGood"]
      };
    },
    getGluImportant() {
      return {
        good: true,
        imortant: !this.data["isImportant"]
      };
    },
    getGluGood() {
      return {
        good: true
      };
    }
  }
};
</script>

<style lang="scss" scoped>
div#form-diagnosa {
  h1#title-form-diagnosa {
    font-size: 32px;
    padding-bottom: 1em;
  }
}
form {
  width: 500px;

  p {
    margin: 0;
    margin-block: 0;
  }
  .form-group {
    margin-top: 20px;

    div.btn-level-group {
      display: flex;

      .btn {
        padding: 10px;
      }
    }

    div {
      margin-top: 5px;

      .btn {
        text-align: center;

        h4 {
          font-weight: 600;
        }
      }

      .good {
        background: #32dbc6;
      }

      .important {
        background: #f6d365;
      }

      .danger {
        background: #f0134d;
      }

      input {
        height: 15px;
        line-height: 15px;
      }

      input,
      select {
        background: #f8f8f8;
        padding: 5px;
        border: none;
        border-radius: 5px;
        text-overflow: ellipsis;
        overflow: hidden;
        color: #888;
        font-family: "Signika", "Arial", sans-serif;

        &:focus {
          outline: none;
          background: #eee;
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

div#button-group {
  width: 100%;
  display: flex;
  justify-content: flex-end;
  margin-top: 30px;

  .btn {
    margin-left: 10px;
    font-weight: 600;
    border-radius: 2px;
  }
}
</style>