<template>
  <div>
    <section id="form-section">
      <FormDiagnosa />
    </section>
  </div>
</template>

<script>
import FormDiagnosa from "@/components/form";

export default {
  scrollToTop: true,
  components: {
    FormDiagnosa
  }
};
</script>

<style lang="scss" scoped></style>
