import { existsSync, writeFileSync } from 'fs';
import { resolve, dirname } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const envFilePath = resolve(__dirname, '../.env');

if (!existsSync(envFilePath)) {
    const defaultEnvContent = `VITE_BASE_URL=/\n`;
    writeFileSync(envFilePath, defaultEnvContent, 'utf8');
    console.log('.env file created with default content');
} else {
    console.log('.env file already exists');
}