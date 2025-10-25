<script setup lang="ts">
  import { computed } from 'vue'
  import { handleBackground } from '@slidev/client/layoutHelper.ts'

  const props = defineProps<{
    imageSrc?: string
    position?: string
  }>()

  const style = computed(() => handleBackground(props.imageSrc, false))
  const flexRow = computed(() => props.position === 'left' ? 'flex-row-reverse' : 'flex-row')
  const textItems = computed(() => props.position === 'left' ? 'items-start' : 'items-end')
  const textAlign = computed(() => props.position === 'left' ? 'text-left' : 'text-right')
</script>

<template>
  <div class="slidev-layout about-me p-0">
    <div class="flex h-full" :class="flexRow">
      <div class="w-1/2 h-full flex flex-col justify-end" :style="style">
      </div>
      <div class="w-1/2 flex flex-col justify-between px-8 py-16" :class="textItems">
        <h1 class="flex">Curiosidades!</h1>

        <div class="flex w-full">
          <img src="/assets/bissexual.png" width="64em" style="display: inline; margin-right: 1em" />
          <img src="/assets/adhd.png" width="64em" style="display: inline; margin-right: 1em" />
          <img src="/assets/dyslexia.png" width="64em" style="display: inline; margin-right: 1em" />
          <img src="/assets/dyscalculia.png" width="64em" style="display: inline; margin-right: 1em" />
          <img src="/assets/high-abilities.png" width="64em" style="display: inline; margin-right: 8px" />
        </div>

        <div class="flex flex-col justify-end text-xl" :class="[textItems, textAlign]">
          <slot />
        </div>
      </div>
    </div>
  </div>
</template>
