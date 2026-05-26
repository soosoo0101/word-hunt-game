// A minimal service worker to satisfy PWA requirements
const CACHE_NAME = 'word-hunt-v1';

self.addEventListener('install', (event) => {
    self.skipWaiting();
});

self.addEventListener('activate', (event) => {
    event.waitUntil(clients.claim());
});

self.addEventListener('fetch', (event) => {
    // We don't cache anything for now, just pass through
    // But having a fetch handler is required for the PWA install prompt in some browsers
    event.respondWith(fetch(event.request));
});
