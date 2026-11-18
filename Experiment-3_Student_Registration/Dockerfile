# Use lightweight Nginx web server
FROM nginx:alpine

# Remove default nginx HTML files
RUN rm -rf /usr/share/nginx/html/*

# Copy HTML, CSS, and JavaScript files to Nginx web root
COPY index.html style.css script.js /usr/share/nginx/html/

# Expose standard HTTP port
EXPOSE 80

# Start Nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]
