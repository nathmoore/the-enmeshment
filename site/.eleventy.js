// Eleventy config for the public site.
// Source of truth for the dossier-page URLs the GPT links to (see
// docs/planning/CONTENT-ARCHITECTURE.md §4). Slugs are FROZEN once published —
// changing a file name changes its URL and breaks archetype-links.txt.
module.exports = function (eleventyConfig) {
  // Passthrough for static assets (CSS/images) once they exist.
  // eleventyConfig.addPassthroughCopy("assets");

  return {
    dir: {
      input: ".",
      includes: "_includes",
      output: "_site",
    },
    markdownTemplateEngine: "njk",
    htmlTemplateEngine: "njk",
    // Project page (now): nathmoore.github.io/the-enmeshment/ → keep "/the-enmeshment/".
    // Custom domain (later: enmeshed.xyz) → flip to "/". Internal links use the `| url`
    // filter so they stay correct under either value. See CONTENT-ARCHITECTURE §4/§5.
    pathPrefix: "/the-enmeshment/",
  };
};
