<script setup>
// import HelloWorld from './components/HelloWorld.vue'
// import TheWelcome from './components/TheWelcome.vue'
import FileFunction from './components/FileFunction.vue'
import MainHeader from './components/MainHeader.vue'
</script>

<template>
  <header>
    <MainHeader />
  </header>

  <main>
    <!-- <TheWelcome /> -->
    <FileFunction />
  </main>
</template>

<style scoped>
header {

}

main {
  margin: auto;
  width: 1080px;
  height: auto;
}
</style>
