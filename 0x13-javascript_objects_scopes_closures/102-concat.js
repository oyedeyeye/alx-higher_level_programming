#!/usr/bin/node
const fs = require('fs').promises;
const files = process.argv.slice(2, 4);

async function concatFile () {
  try {
    // use Promise.all to resolve all promises returned by map
    const data = await Promise.all(
      [...files].map(async element => {
        // use await to resolve the promise returned by readFile
        return await fs.readFile(element, 'utf-8');
      })
    );
    await fs.writeFile(process.argv[4], data.join(''), { flag: 'a' });
  } catch (error) {
    console.error(
      'Got an error trying to write to a file: ' + `${error.message}`
    );
  }
}

(async function () {
  await concatFile();
})();
