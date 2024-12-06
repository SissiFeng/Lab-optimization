"use client"

import { Plus, X, Beaker, Users, Target } from 'lucide-react'
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { Textarea } from "@/components/ui/textarea"
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select"
import { Separator } from "@/components/ui/separator"

export default function OptimizationForm() {
  return (
    <div className="container mx-auto py-8 px-4 bg-gradient-to-br from-blue-50 to-purple-50 min-h-screen">
      <div className="mb-8 text-center">
        <h1 className="text-4xl font-bold tracking-tight text-blue-800 mb-2">Laboratory Optimization Form</h1>
        <p className="text-lg text-blue-600">Configure your laboratory optimization parameters and constraints.</p>
      </div>
      
      <div className="grid gap-8 max-w-4xl mx-auto">
        <Card className="border-t-4 border-t-blue-500 shadow-lg">
          <CardHeader className="bg-gradient-to-r from-blue-100 to-blue-50">
            <CardTitle className="flex items-center text-blue-800">
              <Beaker className="mr-2 h-5 w-5" />
              Laboratory Information
            </CardTitle>
          </CardHeader>
          <CardContent className="space-y-6 pt-6">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div className="space-y-2">
                <Label htmlFor="lab-name" className="text-blue-700">Laboratory Name</Label>
                <Input id="lab-name" placeholder="Enter laboratory name" className="border-blue-200 focus:border-blue-500" />
              </div>
              <div className="space-y-2">
                <Label htmlFor="experiment-name" className="text-blue-700">Experiment Name</Label>
                <Input id="experiment-name" placeholder="Enter experiment name" className="border-blue-200 focus:border-blue-500" />
              </div>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div className="space-y-2">
                <Label htmlFor="duration" className="text-blue-700">Experiment Duration</Label>
                <Input id="duration" placeholder="e.g., 2 weeks" className="border-blue-200 focus:border-blue-500" />
              </div>
              <div className="space-y-2">
                <Label htmlFor="sop" className="text-blue-700">SOP Reference</Label>
                <Input id="sop" placeholder="e.g., SOP-2024-001" className="border-blue-200 focus:border-blue-500" />
              </div>
            </div>
            <div className="space-y-2">
              <Label htmlFor="equipment" className="text-blue-700">Required Equipment</Label>
              <Textarea
                id="equipment"
                placeholder="List required equipment (one per line)"
                className="min-h-[100px] border-blue-200 focus:border-blue-500"
              />
            </div>
          </CardContent>
        </Card>

        <Card className="border-t-4 border-t-purple-500 shadow-lg">
          <CardHeader className="bg-gradient-to-r from-purple-100 to-purple-50">
            <CardTitle className="flex items-center text-purple-800">
              <Users className="mr-2 h-5 w-5" />
              Personnel Requirements
            </CardTitle>
          </CardHeader>
          <CardContent className="space-y-6 pt-6">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div className="space-y-2">
                <Label htmlFor="requirements" className="text-purple-700">Requirements</Label>
                <Textarea
                  id="requirements"
                  placeholder="Describe personnel requirements"
                  className="min-h-[100px] border-purple-200 focus:border-purple-500"
                />
              </div>
              <div className="space-y-2">
                <Label htmlFor="qualifications" className="text-purple-700">Qualifications</Label>
                <Textarea
                  id="qualifications"
                  placeholder="List required qualifications"
                  className="min-h-[100px] border-purple-200 focus:border-purple-500"
                />
              </div>
            </div>
          </CardContent>
        </Card>

        <Card className="border-t-4 border-t-green-500 shadow-lg">
          <CardHeader className="bg-gradient-to-r from-green-100 to-green-50 flex flex-row items-center justify-between">
            <CardTitle className="flex items-center text-green-800">
              <Target className="mr-2 h-5 w-5" />
              Optimization Objectives
            </CardTitle>
            <Button variant="outline" size="sm" className="bg-white hover:bg-green-50 text-green-600 border-green-300">
              <Plus className="mr-2 h-4 w-4" />
              Add Objective
            </Button>
          </CardHeader>
          <CardContent className="space-y-6 pt-6">
            <div className="rounded-lg border border-green-200 p-4 bg-green-50">
              <div className="flex items-start justify-between">
                <div className="grid flex-1 gap-4">
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div className="space-y-2">
                      <Label htmlFor="objective-name" className="text-green-700">Name</Label>
                      <Input id="objective-name" placeholder="Enter objective name" className="border-green-200 focus:border-green-500" />
                    </div>
                    <div className="space-y-2">
                      <Label htmlFor="objective-unit" className="text-green-700">Unit</Label>
                      <Input id="objective-unit" placeholder="e.g., mg/L, °C" className="border-green-200 focus:border-green-500" />
                    </div>
                  </div>
                  <div className="space-y-2">
                    <Label htmlFor="objective-description" className="text-green-700">Description</Label>
                    <Textarea
                      id="objective-description"
                      placeholder="Describe the optimization objective"
                      className="border-green-200 focus:border-green-500"
                    />
                  </div>
                  <div className="space-y-2">
                    <Label htmlFor="objective-priority" className="text-green-700">Priority</Label>
                    <Select defaultValue="medium">
                      <SelectTrigger id="objective-priority" className="border-green-200 focus:border-green-500">
                        <SelectValue placeholder="Select priority" />
                      </SelectTrigger>
                      <SelectContent>
                        <SelectItem value="high">High</SelectItem>
                        <SelectItem value="medium">Medium</SelectItem>
                        <SelectItem value="low">Low</SelectItem>
                      </SelectContent>
                    </Select>
                  </div>
                </div>
                <Button variant="ghost" size="icon" className="text-green-600 hover:text-green-700 hover:bg-green-100">
                  <X className="h-4 w-4" />
                </Button>
              </div>
            </div>
          </CardContent>
        </Card>

        <div className="flex justify-end">
          <Button size="lg" className="bg-blue-600 hover:bg-blue-700 text-white px-8">
            Save Form
          </Button>
        </div>
      </div>
    </div>
  )
}

