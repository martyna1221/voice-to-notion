# Stage 1: Build the application
FROM node:18.17.0 as builder
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci --verbose
COPY . .
RUN npm run build

# Stage 2: Run the application
FROM node:18.17.0-slim
WORKDIR /app

# Copy only the necessary files from the builder stage
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/next.config.mjs ./
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json ./package.json
COPY --from=builder /app/public ./public
COPY --from=builder /app/tailwind.config.js ./tailwind.config.js
COPY --from=builder /app/postcss.config.js ./postcss.config.js

# Expose the port that Cloud Run expects the container to listen on
EXPOSE 8080
ENV PORT=8080

# Start the application
CMD ["npm", "start"]
