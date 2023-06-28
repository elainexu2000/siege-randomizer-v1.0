const sharp = require('sharp');

const imagePath = "website/static/assets/gadgets/Impact_EMP_Grenade.png";

sharp(imagePath)
  .metadata()
  .then(metadata => {
    const imageWidth = metadata.width;
    const imageHeight = metadata.height;
    
    console.log('Image width:', imageWidth, 'pixels');
    console.log('Image height:', imageHeight, 'pixels');
  })
  .catch(err => {
    console.error('Error:', err);
  });