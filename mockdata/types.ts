// ─────────────────────────────────────────────────────────────
// TZ Tourism — TypeScript type definitions
// Generated from Django REST API serializers
// ─────────────────────────────────────────────────────────────

// ── Auth ─────────────────────────────────────────────────────

export interface LoginRequest {
  username: string;
  password: string;
}

export interface LoginResponse {
  access: string;
  refresh: string;
  username: string;
  email: string;
  is_tour_operator: boolean;
}

export interface RegisterRequest {
  username: string;
  email: string;
  password: string;
  password_confirm: string;
  phone?: string;
  bio?: string;
}

export interface UserProfile {
  id: number;
  username: string;
  email: string;
  phone: string;
  bio: string;
  is_tour_operator: boolean;
  date_joined: string; // ISO 8601
}

// ── Region ───────────────────────────────────────────────────

export interface Region {
  id: number;
  name: string;
  slug: string;
  description: string;
  image: string | null;
  latitude: string;
  longitude: string;
  attraction_count: number;
  created_at: string; // ISO 8601
}

// ── Attraction ───────────────────────────────────────────────

export type AttractionCategory =
  | 'mountain'
  | 'beach'
  | 'wildlife'
  | 'cultural'
  | 'historical'
  | 'adventure'
  | 'national_park'
  | 'island'
  | 'waterfall'
  | 'lake'
  | 'other';

export type DifficultyLevel =
  | 'easy'
  | 'moderate'
  | 'challenging'
  | 'difficult'
  | 'extreme';

/** Shape returned by GET /api/v1/attractions/ (list endpoint) */
export interface AttractionListItem {
  id: number;
  name: string;
  slug: string;
  region_name: string;
  category: AttractionCategory;
  category_display: string;
  short_description: string;
  difficulty_level: DifficultyLevel;
  difficulty_display: string;
  featured_image: string | null;
  is_featured: boolean;
  best_time_to_visit: string;
}

/** Shape of a single image in an attraction gallery */
export interface AttractionImage {
  id: number;
  image: string;
  caption: string;
  order: number;
}

/** Shape of a traveller tip */
export interface AttractionTip {
  id: number;
  title: string;
  description: string;
  created_by_username: string | null;
  created_at: string; // ISO 8601
}

/** Shape returned by GET /api/v1/attractions/:slug/ (detail endpoint) */
export interface AttractionDetail {
  id: number;
  name: string;
  slug: string;
  region: Region;
  category: AttractionCategory;
  category_display: string;
  description: string;
  short_description: string;
  latitude: string;
  longitude: string;
  altitude: number | null;
  difficulty_level: DifficultyLevel;
  difficulty_display: string;
  access_info: string;
  nearest_airport: string;
  distance_from_airport: string | null; // decimal as string
  best_time_to_visit: string;
  seasonal_availability: string;
  estimated_duration: string;
  entrance_fee: string | null; // decimal as string, null = free
  requires_guide: boolean;
  requires_permit: boolean;
  featured_image: string | null;
  images: AttractionImage[];
  tips: AttractionTip[];
  is_featured: boolean;
  created_by_username: string | null;
  created_at: string; // ISO 8601
  updated_at: string; // ISO 8601
}

/** Shape for POST/PATCH /api/v1/attractions/ */
export interface AttractionCreateUpdate {
  name: string;
  slug: string;
  region: number; // region ID
  category: AttractionCategory;
  description: string;
  short_description: string;
  latitude: string | number;
  longitude: string | number;
  altitude?: number | null;
  difficulty_level: DifficultyLevel;
  access_info: string;
  nearest_airport?: string;
  distance_from_airport?: string | number | null;
  best_time_to_visit: string;
  seasonal_availability: string;
  estimated_duration: string;
  entrance_fee?: string | number | null;
  requires_guide: boolean;
  requires_permit: boolean;
  featured_image?: File | string | null;
}

// ── Weather ──────────────────────────────────────────────────

/** Shape returned by GET /api/v1/weather/current/?attraction=:slug */
export interface CurrentWeather {
  temperature: number;
  apparent_temperature: number;
  humidity: number;
  precipitation: number;
  rain: number;
  weather_code: number;
  weather_description: string;
  cloud_cover: number;
  wind_speed: number;
  timestamp: string;
}

/** Shape returned by GET /api/v1/weather/forecast/?attraction=:slug */
export interface WeatherForecast {
  dates: string[];              // ["2025-07-15", ...]
  temperature_max: number[];
  temperature_min: number[];
  precipitation: number[];
  rain: number[];
  weather_codes: number[];
}

/** Shape returned by GET /api/v1/weather/seasonal/?attraction=:slug */
export interface SeasonalWeatherPattern {
  id: number;
  season_type: 'dry' | 'short_rain' | 'long_rain';
  season_display: string;
  start_month: number;   // 1–12
  end_month: number;     // 1–12
  avg_temperature: string; // decimal as string
  avg_rainfall: string;    // decimal as string
  description: string;
}

/** Shape returned by GET /api/v1/weather/ (cached list per attraction) */
export interface WeatherCache {
  attraction_name: string;
  temperature: number | null;
  apparent_temperature: number | null;
  precipitation: number | null;
  rain: number | null;
  weather_code: number | null;
  weather_description: string;
  cloud_cover: number | null;
  wind_speed: number | null;
  humidity: number | null;
  last_updated: string; // ISO 8601
}

// ── API error helpers ─────────────────────────────────────────

export interface ApiError {
  detail?: string;
  [field: string]: string | string[] | undefined;
}
