<script setup lang="ts">
  import { computed, ref } from 'vue'
  import QrcodeVue from 'qrcode.vue'

  const props = defineProps<{
    linkedin?: string
    github?: string
    telegram?: string
    bluesky?: string
    heading?: string
    highlight_telegram?: boolean
  }>()

  const heading = computed(() => props.heading ?? 'Redes sociais!')
  const highlightTelegram = computed(() => props.highlight_telegram ?? false)

  import type { Level, RenderAs, GradientType, ImageSettings } from 'qrcode.vue'
  const level = ref<Level>('M')
  const renderAs = ref<RenderAs>('svg')
  const background = ref('transparent')
  const urls = {
    linkedin: props.linkedin,
    github: props.github,
    telegram: props.telegram,
    bluesky: props.bluesky,
  }
  const social = [
    {
      "name": "LinkedIn",
      "foreground": "#0077B5",
      "url": urls.linkedin,
      "image": ref<ImageSettings>({
        src: '/assets/linkedin.svg',
        width: 30,
        height: 30,
        excavate: true,
      })
    },
    {
      "name": "GitHub",
      "foreground": "#282828",
      "url": urls.linkedin,
      "image": ref<ImageSettings>({
        src: '/assets/github.svg',
        width: 30,
        height: 30,
        excavate: true,
      })
    },
    {
      "name": "Telegram",
      "foreground": "#2AABEE",
      "url": urls.linkedin,
      "image": ref<ImageSettings>({
        src: '/assets/telegram.svg',
        width: 30,
        height: 30,
        excavate: true,
      }),
    },
    {
      "name": "BlueSky",
      "foreground": "#4f9bd9",
      "url": urls.linkedin,
      "image": ref<ImageSettings>({
        src: '/assets/bsky.svg',
        width: 30,
        height: 30,
        excavate: true,
      })
    }
  ]

  const gradient = ref(false)
  const gradientType = ref<GradientType>('linear')
  const gradientStartColor = ref('#000000')
  const gradientEndColor = ref('#38bdf8')
</script>

<template>
  <div class="slidev-layout about-me p-0">
    <div class="flex w-full">
      <div class="w-full justify-between px-8 py-14">
        <h1 class="flex">{{ heading }}</h1>
      </div>
    </div>
    <div class="flex h-full w-full">
      <div class="flex w-full grid grid-cols-4 gap-4">
        <div v-for="(item, idx) in social" :key="item.url" class="justify-between px-16 py-8" :style="highlightTelegram && idx !== 2 ? 'opacity: 0.2' : ''">
          <qrcode-vue
            :value="item.url"
            :level="level"
            :render-as="renderAs"
            :background="background"
            :foreground='item.foreground'
            :gradient="gradient"
            :gradient-type="gradientType"
            :gradient-start-color="gradientStartColor"
            :gradient-end-color="gradientEndColor"
            :image-settings='item.image.value'
            :scale="175"
          />
          <div class="text-center text-sm py-12" v-if="highlightTelegram && idx === 2"><h3>Dúvidas?</h3></div>
        </div>
      </div>
    </div>
  </div>
</template>
