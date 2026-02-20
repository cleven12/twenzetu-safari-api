/**
 * TZ Tourism — mock data barrel
 *
 * Drop this entire `mockdata/` folder into your Next.js project root
 * (or anywhere under `src/`) and import from here.
 *
 * Usage:
 *   import { attractions, featuredAttractions, regions } from '@/mockdata'
 *   import type { AttractionListItem, AttractionDetail } from '@/mockdata'
 */

// ── JSON data ────────────────────────────────────────────────
export { default as attractions }        from './attractions.json';
export { default as attractionDetail }   from './attraction-detail.json';
export { default as featuredAttractions} from './featured-attractions.json';
export { default as regions }            from './regions.json';
export { default as weatherMock }        from './weather.json';
export { default as authMock }           from './auth.json';

// ── Types ────────────────────────────────────────────────────
export type {
  // Auth
  LoginRequest,
  LoginResponse,
  RegisterRequest,
  UserProfile,
  // Region
  Region,
  // Attraction
  AttractionCategory,
  DifficultyLevel,
  AttractionListItem,
  AttractionImage,
  AttractionTip,
  AttractionDetail,
  AttractionCreateUpdate,
  // Weather
  CurrentWeather,
  WeatherForecast,
  SeasonalWeatherPattern,
  WeatherCache,
  // Errors
  ApiError,
} from './types';
