<template>
  <div ref="canvas"></div>
  <canvas data-engine="three.js r160" width="1874" height="529" style="width: 1874px; height: 529px;"></canvas>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount, toRefs } from 'vue';
import * as THREE from 'three';

const { canvas } = toRefs(useRefs());

let scene, camera, renderer, particles, lines;

onMounted(() => {
  // Initialize Three.js scene, camera, and renderer
  scene = new THREE.Scene();
  camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
  renderer = new THREE.WebGLRenderer({ canvas: canvas.value, alpha: true });

  renderer.setSize(window.innerWidth, window.innerHeight);

  // Create particles
  const particleGeometry = new THREE.BufferGeometry();
  const particleMaterial = new THREE.PointsMaterial({ color: 0xFFFFFF, size: 0.1 });

  const particlesCount = 1000;
  const particlesPositions = new Float32Array(particlesCount * 3);

  for (let i = 0; i < particlesCount * 3; i++) {
    particlesPositions[i] = (Math.random() - 0.5) * 20;
  }

  particleGeometry.setAttribute('position', new THREE.BufferAttribute(particlesPositions, 3));
  particles = new THREE.Points(particleGeometry, particleMaterial);
  scene.add(particles);

  // Create lines
  const lineGeometry = new THREE.BufferGeometry();
  const lineMaterial = new THREE.LineBasicMaterial({ color: 0xFFFFFF, linewidth: 5 });

  const linesCount = 20;
  const linesPositions = new Float32Array(linesCount * 2 * 3);

  for (let i = 0; i < linesCount * 6; i += 6) {
    linesPositions[i] = -10;
    linesPositions[i + 1] = i / 6 * 10; // Adjust the gap (10px)
    linesPositions[i + 2] = 0;

    linesPositions[i + 3] = 10;
    linesPositions[i + 4] = i / 6 * 10;
    linesPositions[i + 5] = 0;
  }

  lineGeometry.setAttribute('position', new THREE.BufferAttribute(linesPositions, 3));
  lines = new THREE.LineSegments(lineGeometry, lineMaterial);
  scene.add(lines);

  camera.position.z = 5;

  // Animation loop
  const animate = () => {
    requestAnimationFrame(animate);

    // Update particles animation
    const positions = particleGeometry.attributes.position.array;

    for (let i = 0; i < particlesCount * 3; i += 3) {
      positions[i + 1] -= 0.01; // Adjust the speed and direction of particles
      if (positions[i + 1] < -20) positions[i + 1] = 20;
    }

    particleGeometry.attributes.position.needsUpdate = true;

    renderer.render(scene, camera);
  };

  animate();
});

onBeforeUnmount(() => {
  // Clean up resources (optional)
  scene.dispose();
  renderer.dispose();
});
</script>

<style scoped>
/* Add styles if necessary */
</style>
