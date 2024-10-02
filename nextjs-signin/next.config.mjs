/** @type {import('next').NextConfig} */
const nextConfig = {
    reactStrictMode: false,
    eslint: {
      // Warning: This allows production builds to successfully complete even if
      // your project has ESLint errors.
      ignoreDuringBuilds: true,
    },
    images: {
      // domains: ['firebasestorage.googleapis.com', 'images.pexels.com', 'www.pexels.com', 'player.vimeo.com', 'images.unsplash.com', 'source.unsplash.com', 'i.imgur.com', 'img.youtube.com'],
      // domains: ['**'],
      remotePatterns: [
        {
          protocol: 'https',
          hostname: '*',
        },
      ],
    },
  };
  
  export default nextConfig;