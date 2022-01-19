<template>
  <h3>You have / Vous avez <span class="text-danger">{{count}}</span> attempts </h3>
</template>

<script>
export default {
  name: 'Output',
  props: {
    count: Number
  }
}
</script>